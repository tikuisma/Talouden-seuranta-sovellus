import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv('DATABASE_FILE') or 'database.sqlite'
DATABASE_FILE_PATH = os.path.join(dirname, 'data', DATABASE_FILENAME)
USERDATABASE_FILENAME = os.getenv('USERDATABASE_FILE') or 'database.sqlite'
USERDATABASE_FILE_PATH = os.path.join(dirname, 'data', USERDATABASE_FILENAME)
print(DATABASE_FILE_PATH)
print(USERDATABASE_FILE_PATH)
