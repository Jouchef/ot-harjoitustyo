import sys
import os
from config import DATABASE_NAME
import sqlite3


dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, DATABASE_NAME))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
