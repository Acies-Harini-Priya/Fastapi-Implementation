from ..models.dtos.update_intern_body import UpdateInternBody
from ..models.dtos.add_new_intern_body import AddNewInternBody
from ..repositories.repository import InternsRepository
from ..utils.dataframe_to_json import dataFrameToJson
from fastapi import HTTPException
from ..constants import ERROR
from ..constants import MESSAGE
from ...app import constants


class InternsService:
    def __init__(self):
        self.intern_repo = InternsRepository()

    def fetch_interns_details(self):
        status_code, dataframe = self.intern_repo.fetch_all_interns()
        if not dataframe or dataframe.empty:
            return 500, {ERROR: constants.DATA_NOT_FOUND_MESSAGE}
        response_data = dataFrameToJson(dataframe)
        return 200, response_data

    def fetch_interns_details_by_name(self, name: str):
        status_code, dataframe = self.intern_repo.fetch_interns_by_name(name)
        if not dataframe or dataframe.empty:
            return 500, {ERROR: constants.DATA_NOT_FOUND_MESSAGE}
        response_data = dataFrameToJson(dataframe)
        return 200, response_data

    def add_new_intern(self, body: AddNewInternBody):
        values = (body.name, body.mail_id, body.dob, body.college_name, body.description, body.hobbies, 
                  body.created_by, body.updated_by, body.created_at, body.updated_at)
        status_code, message = self.intern_repo.add_intern(values)
        if status_code != 200:
            return 500, {MESSAGE: constants.FAILED_TO_ADD_MESSAGE}
        return 200, {MESSAGE: constants.ADD_INTERN_SUCCESS_MESSAGE}

    def update_intern_by_name(self, name: str, body: UpdateInternBody):
        values = (body.name, body.mail_id, body.dob, body.college_name, body.description, body.hobbies,
                  body.updated_by, body.updated_at, name)
        status_code, message = self.intern_repo.update_intern(values)
        if status_code != 200:
            raise HTTPException(status_code, message)
        return {MESSAGE: constants.UPDATE_INTERN_SUCCESS_MESSAGE}

    def delete_intern_by_name(self, name: str):
        status_code, message = self.intern_repo.delete_intern(name)
        if status_code != 200:
            raise HTTPException(status_code, message)
        return {MESSAGE: constants.DELETE_INTERN_SUCCESS_MESSAGE}
