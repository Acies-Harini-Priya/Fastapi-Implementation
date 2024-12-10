from typing import Union

from fastapi import APIRouter, FastAPI, logger

from backend.dev.routes.InternsInfo import InternsInfo
from backend.dev.routes.dto.UpdateInternBody import UpdateInternBody
from backend.dev.routes.dto.AddNewInternBody import AddNewInternBody

interns_info_router  = APIRouter(
    prefix="/InternsInfo",
    tags=["InternsInformation"],
    responses={404: {"description": "Not Found in /InternsInfo"}},
)

interns_info = InternsInfo()

## get 
@interns_info_router.get("/fetchInternsDetails")
async def fetchDetails():
    print(f"fetchInternsDetails started")
    response_code, response_data = interns_info.fetchInternsDetails()
    print(f"fetchInternsDetails ended")
    return response_data

## get 
@interns_info_router.get("/fetchInternDetailsByName")
async def fetchDetailsByName(name: str):
    print(f"fetchInternDetailsByName started with request data {name}")
    response_code, response_data = interns_info.fetchInternsDetailsByName(name)
    print(f"fetchInternDetailsByName ended with request data {name}")
    return response_data


## post
@interns_info_router.post("/addNewIntern")
async def fetchDetailsByName(body: AddNewInternBody):
    print(f"addNewIntern started with request data {body}")
    response_data = interns_info.addNewIntern(body)
    print(f"addNewIntern ended with request data {body}")
    return response_data

## put
@interns_info_router.put("/updateInternDetails/{name}")
async def updateInternDetails(name: str, body: UpdateInternBody):
    print(f"updateInternDetails started with ID: {name} and request data: {body}")
    response_data = interns_info.updateInternDetailsById(name, body)
    print(f"updateInternDetails ended with ID: {name} and request data: {body}")
    return response_data

## patch - partial update
# @interns_info_router.post("/updateInternDetails")
# async def updateInternDetails(body: UpdateInternBody):
#     print(f"updateInternDetails started with request data {body}")
#     response_data = interns_info.updateInternDetailsById(body)
#     print(f"updateInternDetails ended with request data {body}")
#     return response_data

## delete
@interns_info_router.delete("/deleteIntern/{name}")
async def deleteIntern(name:str):
    print(f"deleteIntern started with request data {name}")
    response_data = interns_info.deleteInternById(name)
    print(f"deleteIntern ended with request data {name}")
    return response_data
