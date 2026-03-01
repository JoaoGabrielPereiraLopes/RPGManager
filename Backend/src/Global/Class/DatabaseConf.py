import os
from dotenv import load_dotenv
import psycopg2
load_dotenv()  # carrega o .env

class DB:
    def __init__(self):
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")

        self.connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )
        self.cursor=self.connection.cursor()
    def startDatabase(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT NOW(),
            nickname VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
            );
        """

        self.cursor.execute(create_table_query)
        self.connection.commit()
        self.cursor.close()