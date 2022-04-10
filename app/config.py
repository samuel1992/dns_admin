# TODO: import database stuff from env variables
import os


class Config():
    DEBUG = True
    DATABASE_NAME = 'dns_admin'
    DATABASE_USER = 'dns_admin_usr'
    DATABASE_PASSWORD = 'dns@321'
    PORT = '5000'
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
