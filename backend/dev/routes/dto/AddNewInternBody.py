from pydantic import BaseModel

class AddNewInternBody(BaseModel):
    name: str
    mail_id: str
    dob: str
    college_name: str
    description: str 
    hobbies: str
    created_by: str
    updated_by: str
    created_at: str
    updated_at: str

    # image: str


