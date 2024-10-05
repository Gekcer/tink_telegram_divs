import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

class DBConnector:
    def __init__(self):
        self.engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    def get_engine(self):
        pass


if __name__ == '__main__':
    dc = DBConnector()
    print(dc.engine)