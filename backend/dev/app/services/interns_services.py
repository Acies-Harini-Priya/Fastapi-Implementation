from ..models.dtos.update_intern_body import UpdateInternBody
from ..models.dtos.add_new_intern_body import AddNewInternBody

from ..repositories.repository import InternsRepository
from ..utils.dataframe_to_json import dataFrameToJson
from ..constants import MESSAGE
from ...app import constants


class InternsService:
    def __init__(self):
        self.intern_repo = InternsRepository()

    def fetch_interns_details(self):
        intern_dataframe, message = self.intern_repo.fetch_all_interns()
        response_data = dataFrameToJson(intern_dataframe)
        return 200, response_data

    def fetch_interns_details_by_name(self, name: str):
        intern_dataframe, message = self.intern_repo.fetch_interns_by_name(name)
        response_data = dataFrameToJson(intern_dataframe)
        return 200, response_data

    def add_new_intern(self, body: AddNewInternBody):
        values = (body.name, body.mail_id, body.dob, body.college_name, body.description, body.hobbies)
        rows_affected, message = self.intern_repo.add_intern(values)
        if rows_affected < 0:
            return 500, {MESSAGE: constants.FAILED_TO_ADD_MESSAGE}
        else:
            return 200, {MESSAGE: constants.ADD_INTERN_SUCCESS_MESSAGE}

    def update_intern_by_id(self, id: int, body: UpdateInternBody):
        values = (body.name, body.mail_id, body.dob, body.college_name, body.description, body.hobbies, id)
        rows_affected, message = self.intern_repo.update_intern(values)
        if rows_affected < 0:
            return 500, {MESSAGE: constants.FAILED_TO_ADD_MESSAGE}
        else:
            return 200, {MESSAGE: constants.UPDATE_INTERN_SUCCESS_MESSAGE}

    def delete_intern_by_id(self, id: int):
        status_code, message = self.intern_repo.delete_intern(id)
        return {MESSAGE: constants.DELETE_INTERN_SUCCESS_MESSAGE}
