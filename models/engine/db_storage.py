#!/usr/bin/python3
""" New Engine as DBStorage """
import models
from os import getenv
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session, relationship

class DBStorage:
    """This class defines the DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Function called every time a new object is created"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, database), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        """If 'Test mode' drop all tables"""
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Shows all data from defined classes"""
        if cls:
            objs = self.__session.query(cls).all()

        else:
            classes = [State, City, User, Place, Review, Amenity]
            objs = []
            for cls in classes:
                objs += self.__session.query(cls)

    def all(self, cls=None):
        """ShowS all data from defined classes"""
        if cls:
            objs = self.__session.query(cls).all()

        else:
            classes = [State, City, User, Place, Review, Amenity]
            objs = []
            for cls in classes:
                objs += self.__session.query(cls)

    def new(self, obj):
        """Creates a new instance of the class passed as an argument"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Recreeates database and it's tables"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session

    def close(self):
        """Closes current session"""
        self.__session.close()
