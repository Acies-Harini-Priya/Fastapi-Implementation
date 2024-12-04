from typing import Union

from fastapi import APIRouter, FastAPI, logger

from backend.dev.routes.InternsInfo import InternsInfo

interns_info_router  = APIRouter(
    prefix="/InternsInfo",
    tags=["InternsInfo"],
    responses={404: {"description": "Not Found in /InternsInfo"}},
)

interns_info = InternsInfo()
@interns_info_router.get("/")
def read_root():
    return {"Hello": "World"}

## Read
@interns_info_router.get("/fetchInternsDetailsByName")
async def fetchDetails():
    logger.info(f"fetchInternsDetails started")
    response_code, response_data = interns_info.fetchInternsDetails()
    # response_object = CustomJSONResponse(
    #     status_code=response_code, content=response_data
    # )
    logger.info(f"fetchInternsDetails ended")
    return response_data


#

## Create


## Update


## Delete

