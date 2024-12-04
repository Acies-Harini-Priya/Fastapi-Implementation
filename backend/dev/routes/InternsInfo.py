from psycopg2 import sql

from backend.dev.utils.BaseExecutor import BaseExecutor
from backend.dev.utils.dataframe_to_json import dataFrameToJson

base_executor = BaseExecutor()
class InternsInfo:
    def fetchInternsDetails(self):
        query = sql.SQL(f""" 
                
            """)
        dataframe , message = base_executor.executeSelect(query=query, values=(body.id,), get_as_packet=True)
        response_data = dataFrameToJson(dataframe)
        return 200, response_data