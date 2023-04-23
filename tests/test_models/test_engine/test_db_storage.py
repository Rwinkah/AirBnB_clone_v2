#!/usr/bin/python3
""" tests for db storage """
import unittest
from models.base_model import BaseModel
import MySQLdb
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'filestorage test not supported')
class test_db_storage(unittest.TestCase):
    """ class to test db storage engine """

    def setup(self):
        """ create test env """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.get_env('HBNB_MYSQL_DB')

        self.connt = msq.connect(user=user, host=host, db=db, passwd=pwd)
        self.curs = connt.cursor()
        self.curs.execute("CREATE DATABASE IF NOT EXISTS test_db")
        self.curs.execute("CREATE TABLE IF NOT EXISTS state")

    def teardowm(self):
        """ cleanup after test """
        self.curs.execute("DROP DATABASE IF EXISTS test_db")
        self.curs.close()
        self.connt.close()
