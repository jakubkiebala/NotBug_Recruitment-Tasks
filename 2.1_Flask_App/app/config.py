from psycopg2 import connect

settings = {
    'host': 'localhost',
    'database': 'flask_app_jk',
    'user': 'user',
    'password': 'password',
    'port': '5432'
}


def connect_to_db():
    connection = connect(
        **settings
    )
    return connection
