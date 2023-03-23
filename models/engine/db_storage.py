#!/usr/bin/python3
""" Creating DB Storage """

import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
nameClass = {'Amenity': Amenity, 'City': City,
             'Place': Place, 'State': State,
             'Review': Review, 'User': User}
 
class DBStorage():
    """ This class handsles db storage for hbnb"""
    def __init__(self):
        """init the storage """

        password = os.getenv('HBNB_MYSQL_PWD')
        user = os.getenv('HBNB_MYSQL_USER')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                       user, password, host, database))
        self.__sessionInst = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = sessionInst()

    def all(self, cls=None):
        """ returns an object containing all objects 
        or all objects of a class if specifiedn"""

        objects = {}
        if type(cls) == str and cls in nameClass:
            all_cls = self.__session.query(cls)
            for obj in all_cls:
                objects[(cls + '.' + obj.id)] = obj
        else:
            for cls in nameClass.values():
                for obj in self.__session.query(cls):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def new(self, obj):
        """ stages a new obj to be added to database """
        self.__session.add(obj)

    def reload(self):
        """ load data from a database """
        Base.metadata.create_all(self.__engine)
        self.__session = self.__sessionInst()

    def save(self):
        """ save changes to the database """
        self.__session.commit()
