from http.client import HTTPException
import os
from dotenv import load_dotenv
from psycopg2 import sql
from backend.dev.routes.dto.UpdateInternBody import UpdateInternBody
from backend.dev.routes.dto.AddNewInternBody import AddNewInternBody
from backend.dev.utils.BaseExecutor import BaseExecutor
from backend.dev.utils.dataframe_to_json import dataFrameToJson

# get values from .env
load_dotenv(dotenv_path=f"{os.getcwd()}\\backend\\dev\\envs\\.env")
db_config = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    
}

print(db_config)
base_executor = BaseExecutor(db_config=db_config)
class InternsInfo:
    def fetchInternsDetails(self):
        query = sql.SQL(f""" 
                select * 
                from fastapi_demo.interns_details
            """)
        dataframe , message = base_executor.executeSelect(query=query, values=(), get_as_packet=True)
        if dataframe is None or dataframe.empty:
            return 500, {"error": "No data found or query failed."}
        response_data = dataFrameToJson(dataframe)
        return 200, response_data
    
    def fetchInternsDetailsByName(self,name:str):
        query = sql.SQL(f""" 
                select * 
                from fastapi_demo.interns_details
                where name = %s
            """)
        dataframe , message = base_executor.executeSelect(query=query, values=(name,), get_as_packet=True)
        if dataframe is None or dataframe.empty:
            return 500, {"error": "No data found or query failed."}
        response_data = dataFrameToJson(dataframe)
        return 200, response_data
    
    
    def addNewIntern(self,body: AddNewInternBody):
        query = sql.SQL("""
            insert into 
                fastapi_demo.interns_details
                (name, 
                mail_id, 
                dob, 
                college_name, 
                description, 
                hobbies, 
                created_by, 
                updated_by, 
                created_at, 
                updated_at)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """)

        #(image_url is omitted, so NULL will be used)
        values = (body.name, body.mail_id, body.dob, body.college_name, 
                body.description, body.hobbies, body.created_by,
                body.updated_by,body.created_at,body.updated_at)
        try:
            rows_affected, message = base_executor.executeInsert(query=query, values=values)
            if rows_affected > 0:
                return 200, {"message": "Added Intern successfully."}
            else:
                return 500, {"message": "Failed to add Intern."}
        except Exception as e:
            return 500, {"message": f"An error occurred: {str(e)}"}

    def updateInternDetailsById(self, name: str, body: UpdateInternBody):
        query = sql.SQL(f"""
            update fastapi_demo.interns_details
            set 
                mail_id = %s,
                dob = %s,
                college_name = %s,
                description = %s,
                hobbies = %s,
                updated_by = %s,
                updated_at = %s
            where name = %s
        """)

        values = (body.mail_id, body.dob, body.college_name,
            body.description, body.hobbies, body.updated_by,
            body.updated_at, name,
        )
        print(f"Executing query: {query}")
        print(f"With values: {values}")

        try:
            rows_affected, message = base_executor.executeUpdate(query=query, values=values)
            if rows_affected == 0:
                raise HTTPException(404, "No record found with the given ID.")
            return {"message": "Intern details updated successfully."}
        except Exception as e:
            raise HTTPException(500, f"An error occurred: {str(e)}")
            
    def deleteInternById(self,name:str):
        query = sql.SQL(f"""
            delete from fastapi_demo.interns_details
            where name = %s
        """)
        
        values = (name,)
        try:
            rows_affected, message = base_executor.executeDelete(query=query, values=values)
            if rows_affected > 0:
                return {"message": "Intern deleted successfully."}
            else:
                raise HTTPException(500, "Failed to delete Intern.")
        except Exception as e:
            raise HTTPException(500, f"An error occurred: {str(e)}")