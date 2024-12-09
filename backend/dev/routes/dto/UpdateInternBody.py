from pydantic import BaseModel

class UpdateInternBody(BaseModel):
    name: str
    mail_id: str
    dob: str
    college_name: str
    description: str 
    hobbies: str
    updated_by: str
    updated_at: str
    
    # image: str


