from psycopg2 import sql

class InternsQueries:
    FETCH_ALL_INTERNS = sql.SQL("""
        select * 
        from fastapi_demo.interns_details
    """)

    FETCH_BY_NAME = sql.SQL("""
        select * 
        from fastapi_demo.interns_details
        where name = %s
    """)

    INSERT_NEW_INTERN = sql.SQL("""
        insert into 
            fastapi_demo.interns_details
            (name, mail_id, dob, college_name, description, hobbies)
        values (%s, %s, %s, %s, %s, %s)
    """)

    UPDATE_INTERN_BY_NAME = sql.SQL("""
        update fastapi_demo.interns_details
        set 
            name = %s,
            mail_id = %s,
            dob = %s,
            college_name = %s,
            description = %s,
            hobbies = %s
        where name = %s
    """)

    DELETE_INTERN_BY_NAME = sql.SQL("""
        delete from fastapi_demo.interns_details
        where name = %s
    """)
