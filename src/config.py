import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    #Pytest will use other .env file and it will be loaded with pytest.ini -file.
    load_dotenv(os.path.join(dirname, ".env"))
except FileNotFoundError:
    pass

DATABASE_NAME = os.getenv("DATABASE_NAME") or "database.sqlite"
CALENDAR_PRICE = os.getenv("CALENDAR_PRICE") or 10
