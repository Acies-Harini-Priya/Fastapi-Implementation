from ..config.config import db_config
from ..repositories.base_executor import BaseExecutor
from ..repositories.queries import InternsQueries

class InternsRepository:
    def __init__(self):
        self.base_executor = BaseExecutor(db_config=db_config)

    def fetch_all_interns(self):
        return self.base_executor.executeSelect(query=InternsQueries.FETCH_ALL_INTERNS, values=(), get_as_packet=True)

    def fetch_interns_by_name(self, name: str):
        return self.base_executor.executeSelect(query=InternsQueries.FETCH_BY_NAME, values=(name,), get_as_packet=True)

    def add_intern(self, values):
        return self.base_executor.executeInsert(query=InternsQueries.INSERT_NEW_INTERN, values=values)

    def update_intern(self, values):
        return self.base_executor.executeUpdate(query=InternsQueries.UPDATE_INTERN_BY_NAME, values=values)

    def delete_intern(self, name: str):
        return self.base_executor.executeDelete(query=InternsQueries.DELETE_INTERN_BY_NAME, values=(name,))
