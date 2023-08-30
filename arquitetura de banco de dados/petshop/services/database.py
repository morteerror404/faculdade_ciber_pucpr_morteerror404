from sqlalchemy_utils import database_exist, create_database
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from urllib.parse import quote

instance = f"mysql+pymysql://test:{quote('test')}@localhost:3307/petshop"

if not database_exist(url = instance):
    create_database(url= instance)
    
engine = create_engine(url= instance)
session = Session (bind = engine, autoflush =True)