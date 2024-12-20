from fastapi import APIRouter
from ..services.interns_services import InternsService
from ..models.dtos.add_new_intern_body import AddNewInternBody
from ..models.dtos.update_intern_body import UpdateInternBody


router = APIRouter()
interns_service = InternsService()

@router.get("/fetchInternDetails")
async def get_interns():
    return interns_service.fetch_interns_details()

@router.get("/fetchInternDetailsByName/{name}")
async def get_intern_by_name(name: str):
    return interns_service.fetch_interns_details_by_name(name)

@router.post("/addNewIntern")
async def add_intern(body: AddNewInternBody):
    return interns_service.add_new_intern(body)

@router.put("/updateInternDetails/{id}")
async def update_intern(id: int, body: UpdateInternBody):
    return interns_service.update_intern_by_id(id, body)

@router.delete("/deleteIntern/{id}")
async def delete_intern(id: int):
    return interns_service.delete_intern_by_id(id)
