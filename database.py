from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import urllib


load_dotenv()

PASSWORD = os.getenv('PASSWORD')
USERNAME = os.getenv('USERNAME')
DRIVER = os.getenv('DRIVER')
DATABASE = os.getenv('DATABASE')
SERVER = os.getenv('SERVER')

params = urllib.parse.quote_plus(
    'Driver=%s;' % DRIVER +
    'Server=tcp:%s,1433;' % SERVER +
    'Database=%s;' % DATABASE +
    'Uid=%s;' % USERNAME +
    'Pwd={%s};' % PASSWORD +
    'Encryption=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=30;'

)

conn_string = 'mssql+pyodbc:///?odbc_connect=' + params

engine = create_engine(conn_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
