import psycopg2
from psycopg2 import sql
import pandas as pd

class BaseExecutor:
    def __init__(self, db_config):
        """
        Initialize the database connection configuration.
        
        Args:
            db_config (dict): A dictionary with keys: dbname, user, password, host, port.
        """
        self.db_config = db_config

    def executeSelect(self, query, values=None, get_as_packet=False):
        """
        Executes a SELECT query and fetches the results.

        Args:
            query (sql.SQL): The query to be executed.
            values (tuple): Parameters for the query.
            get_as_packet (bool): Whether to return results as a Pandas DataFrame.

        Returns:
            tuple: (data, message)
        """
        try:
            # Connect to the database
            connection = psycopg2.connect(**self.db_config)
            cursor = connection.cursor()

            # Execute the query
            cursor.execute(query, values)

            # Fetch all results
            rows = cursor.fetchall()
            col_names = [desc[0] for desc in cursor.description]

            if get_as_packet:
                # Convert to Pandas DataFrame
                dataframe = pd.DataFrame(rows, columns=col_names)
                return dataframe, "Query executed successfully."
            else:
                return rows, "Query executed successfully."

        except psycopg2.Error as e:
            return None, f"Database error: {e}"
        finally:
            # Ensure resources are cleaned up
            if cursor:
                cursor.close()
            if connection:
                connection.close()
