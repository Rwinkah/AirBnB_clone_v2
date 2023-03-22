#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if (os.getenv('HBTN_TYPE_STORAGE') == 'db'):
    storage = DBStorage()
else:
    stoage = FileStorage()

storage.reload()
