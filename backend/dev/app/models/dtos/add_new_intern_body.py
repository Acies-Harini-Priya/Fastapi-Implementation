from pydantic import BaseModel

class AddNewInternBody(BaseModel):
    name: str
    mail_id: str
    dob: str
    college_name: str
    description: str 
    hobbies: str



