import uvicorn
from fastapi import FastAPI
from fastapi.openapi.models import Response
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import HTTPException
from starlette import status #starlette  is imported to use async api
from fastapi.middleware.cors import CORSMiddleware
import os
from routes.InternsInfoRouter import interns_info_router
from dotenv import load_dotenv

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost",
]

load_dotenv('.env')
app = FastAPI()

app.add_middleware( #middleware connects backend with api
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router=interns_info_router)
    
if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv
    import os

    # Load environment variables
    load_dotenv(dotenv_path=f"{os.getcwd()}\\backend\\dev\\envs\\.env")

    uvicorn.run("__main__:app", host="0.0.0.0", port=int(os.getenv('API_PORT')), reload=True)

