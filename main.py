from logic import DB_Manager
from config import *

if __name__ == "__main__":
    manager = DB_Manager(DATABASE)
    manager.create_tables()
