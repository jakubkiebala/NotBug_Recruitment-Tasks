import psycopg2
from app.config import settings


def create_database():
    conn = psycopg2.connect(
        host=settings['host'],
        user=settings['user'],
        password=settings['password'],
        port=settings['port'],
        database="postgres"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    query = 'CREATE DATABASE flask_app_jk;'


    try:
        cursor.execute(query)
        print('Data base has been created')
    except psycopg2.errors.DuplicateDatabase:
        print('Data base was already created')

    cursor.close()
    conn.close()


def create_tables():
    conn = psycopg2.connect(**settings)
    cursor = conn.cursor()


    with open('migrations/schema.sql', 'r') as file:
        schema = file.read()

    cursor.execute(schema)
    conn.commit()
    print("Tables have been created.")

    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_database()
    create_tables()


def create_database_with_tables():
    
    create_database()
    create_tables()
    return None

