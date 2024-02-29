import os
from os import environ, path, system
from typing import Any
from dotenv import load_dotenv


BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

"""Note: The Config class is at the bottom because it instantiates the other classes in this file"""


class DbConfig:
    """Set the Database configuration variables from the .env file"""
    """NOTE: Only SQLite, MySQL, & PostgreSQL are working currently"""
    """NOTE: MySQL Unix Sockets is currently un-supported"""
    db_type = environ.get('DB_TYPE')
    db_name = environ.get('DB_NAME')
    db_hostname = environ.get('DB_HOSTNAME')
    db_username = environ.get('DB_USERNAME')
    db_password = environ.get('DB_PASSWORD')
    db_port = environ.get('DB_PORT')
    db_connection_type = environ.get('DB_CONNECTION_TYPE')
    db_unix_socket = environ.get('DB_UNIX_SOCKET')

    if db_type == 'sqlite':
        uri = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

    if db_type == 'mysql':
        if db_connection_type == 'socket':
            uri = 'mysql:///' + db_name + '?' + db_unix_socket
        else:
            uri = "mysql://" + db_username + ':' + db_password + '@' + db_hostname + ':' + db_port + '/' + db_name

    if db_type == 'postgresql':
        uri = 'postgresql://' + db_username + ':' + db_password + '@' + db_hostname + ':' + db_port + '/' + db_name


class AdminsDbConfig:
    """Set the Admins Database configuration variables from the .env file"""
    """NOTE: Only SQLite, MySQL, & PostgreSQL are working currently"""
    """NOTE: MySQL Unix Sockets is currently un-supported"""
    db_use_admins_database = environ.get('DB_USE_ADMINS_DATABASE')
    db_type = environ.get('DB_ADMINS_DATABASE_TYPE')
    db_name = environ.get('DB_ADMINS_DATABASE_NAME')
    db_hostname = environ.get('DB_ADMINS_DATABASE_HOSTNAME')
    db_username = environ.get('DB_ADMINS_DATABASE_USERNAME')
    db_password = environ.get('DB_ADMINS_DATABASE_PASSWORD')
    db_port = environ.get('DB_ADMINS_DATABASE_PORT')
    db_connection_type = environ.get('DB_ADMINS_DATABASE_CONNECTION_TYPE')
    db_unix_socket = environ.get('DB_ADMINS_DATABASE_UNIX_SOCKET')

    if db_use_admins_database == 'True' or db_use_admins_database == 'true':

        if db_type == 'sqlite':
            uri = 'sqlite:///' + os.path.join(BASE_DIR, 'admins.db')

        if db_type == 'mysql':
            if db_connection_type == 'socket':
                uri = 'mysql:///' + db_name + '?' + db_unix_socket
            else:
                uri = "mysql://" + db_username + ':' + db_password + '@' + db_hostname + ':' + db_port + '/' + db_name

        if db_type == 'postgresql':
            uri = 'postgresql://' + db_username + ':' + db_password + '@' + db_hostname + ':' + db_port + '/' + db_name


class UsersDbConfig:
    """Set the Users Database configuration variables from the .env file"""
    """NOTE: Only SQLite, MySQL, & PostgreSQL are working currently"""
    """NOTE: MySQL Unix Sockets is currently un-supported"""
    db_use_users_database = environ.get('DB_USE_USERS_DATABASE')
    db_type = environ.get('DB_USERS_DATABASE_TYPE')
    db_name = environ.get('DB_USERS_DATABASE_NAME')
    db_hostname = environ.get('DB_USERS_DATABASE_HOSTNAME')
    db_username = environ.get('DB_USERS_DATABASE_USERNAME')
    db_password = environ.get('DB_USERS_DATABASE_PASSWORD')
    db_port = environ.get('DB_USERS_DATABASE_PORT')
    db_connection_type = environ.get('DB_USERS_DATABASE_CONNECTION_TYPE')
    db_unix_socket = environ.get('DB_USERS_DATABASE_UNIX_SOCKET')

    if db_use_users_database == 'True' or db_use_users_database == 'true':

        if db_type == 'sqlite':
            uri = 'sqlite:///' + os.path.join(BASE_DIR, 'users.db')

        if db_type == 'mysql':
            if db_connection_type == 'socket':
                uri = 'mysql:///' + db_name + '?' + db_unix_socket
            else:
                uri = "mysql://" + db_username + ':' + db_password + '@' + db_hostname + ':' + db_port + '/' + db_name

        if db_type == 'postgresql':
            uri = 'postgresql://' + db_username + ':' + db_password + '@' + db_hostname + ':' + db_port + '/' + db_name


class SessionsConfig:
    """Set the Session configuration variables from the .env file"""
    """Reference: https://flask-session.readthedocs.io/en/latest/config.html"""
    session_type = environ.get('SESSION_TYPE')
    session_permanent = environ.get('SESSION_PERMANENT')
    session_cookie_secure = environ.get('SESSION_COOKIE_SECURE')
    session_fild_dir = os.path.join(BASE_DIR, environ.get('SESSION_FILE_DIR'))
    session_file_mode = environ.get('SESSION_FILE_MODE')
    session_file_threshold = environ.get('SESSION_FILE_THRESHOLD')
    # Whether sign the session cookie sid or not.
    # If enabled, flask.Flask.secret_key must be set, default is 'False'
    session_use_signer = environ.get('SESSION_USE_SIGNER')

    # Session-Redis
    if session_type == 'redis':
        # A redis.Redis instance (Default: 127.0.0.1:6379
        session_redis = environ.get('SESSION_REDIS')

    # Session-Memcached
    if session_type == 'memcached':
        # A memcache.Client instance (Default: 127.0.0.1:11211)
        session_memcached = environ.get('SESSION_MEMCACHED')

    # Session-MongoDB
    if session_type == 'mongodb':
        # A pymongo.MongoClient instance
        session_mongodb = environ.get('SESSION_MONGODB')
        # set the MongoDB Database (Default: flask_session)
        session_mongodb_db = environ.get('SESSION_MONGODB_DB')
        # Set the MongoDB Collection (Default: sessions)
        session_mongodb_collect = environ.get('SESSION_MONGODB_COLLECT')

    # Session-SQLAlchemy
    if session_type == 'sqlalchemy':
        # A flask_sqlalchemy.SQLAlchemy instance
        session_sqlalchemy = environ.get('SESSION_SQLALCHEMY')
        # Set the SQLAlchemy database table
        session_sqlalchemy_table = environ.get('SESSION_SQLALCHEMY_TABLE')


class SessionsDbConfig:
    """Set the Session Database configuration variables from the .env file"""
    """NOTE: Only SQLite, MySQL, & PostgreSQL are working currently"""
    """NOTE: MySQL Unix Sockets is currently un-supported"""
    db_type = environ.get('DB_SESSIONS_DATABASE_TYPE')
    db_name = environ.get('DB_SESSIONS_DATABASE_NAME')
    db_hostname = environ.get('DB_SESSIONS_DATABASE_HOSTNAME')
    db_username = environ.get('DB_SESSIONS_DATABASE_USERNAME')
    db_password = environ.get('DB_SESSIONS_DATABASE_PASSWORD')
    db_port = environ.get('DB_SESSIONS_DATABASE_PORT')
    db_connection_type = environ.get('DB_SESSIONS_DATABASE_CONNECTION_TYPE')
    db_unix_socket = environ.get('DB_SESSIONS_DATABASE_UNIX_SOCKET')

    if db_type == 'sqlite':
        uri = 'sqlite:///' + os.path.join(BASE_DIR, 'sessions.db')

    if db_type == 'mysql':
        if db_connection_type == 'socket':
            uri = 'mysql:///' + db_name + '?' + db_unix_socket
        else:
            uri = "mysql://" + db_username + ':' + db_password + '@' + db_hostname + ':' + db_port + '/' + db_name

    if db_type == 'postgresql':
        uri = 'postgresql://' + db_username + ':' + db_password + '@' + db_hostname + ':' + db_port + '/' + db_name
        

class MailConfig:
    """Set the Flask-Mail configuration variables from the .env file"""
    mail_server = environ.get('MAIL_SERVER')
    mail_port = environ.get('MAIL_PORT')
    mail_username = environ.get('MAIL_USERNAME')
    mail_password = environ.get('MAIL_PASSWORD')
    mail_use_tls = environ.get('MAIL_USE_TLS')
    mail_use_ssl = environ.get('MAIL_USE_SSL')
    mail_debug = environ.get('MAIL_DEBUG')
    mail_default_sender = environ.get('MAIL_DEFAULT_SENDER')
    mail_max_emails = environ.get('MAIL_MAX_EMAILS')
    mail_suppress_send = environ.get('MAIL_SUPPRESS_SEND')
    mail_ascii_attachments = environ.get('MAIL_ASCII_ATTACHMENTS')



class Config:
    """Set Flask configuration variables from .env file."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")

    # Flask Config
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Flask-Session (redis)
    # REDIS_URI = environ.get("REDIS_URI")
    # SESSION_TYPE = "redis"
    # SESSION_REDIS = redis.from_url(REDIS_URI)

    # Flask-Session (filesystem)
    SESSION_TYPE = environ.get('SESSION_TYPE')
    SESSION_PERMANENT = environ.get('SESSION_PERMANENT')

    # Flask-SQLAlchemy
    Db_Config = DbConfig()
    Users_Db_Config = UsersDbConfig()
    Admins_Db_Config = AdminsDbConfig()
    SQLALCHEMY_DATABASE_URI = Db_Config.uri
    SQLALCHEMY_DATABASE_URI_ADMINS = Admins_Db_Config.uri
    SQLALCHEMY_DATABASE_URI_USERS = Users_Db_Config.uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Flask-Assets (Optional)
    LESS_BIN = system("which lessc")
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")