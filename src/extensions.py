__author__ = "Suvesh Agnihotri"
__copyright__ = "Copyright 2018 Minance. All rights reserved"
__status__ = "Development"
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

jwt = JWTManager()
db = SQLAlchemy()
