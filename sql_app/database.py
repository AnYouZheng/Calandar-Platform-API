import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")
load_dotenv()

class DB_connect:

    #從.env 抓出SQL詳細資料
    host = os.getenv('host')
    user = os.getenv('user')
    password = os.getenv('password')
    database = os.getenv('database')
    
    #定義DB 位址
    SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://user:password@host/database' 
    
    #創建SQLalchmy引擎並連接
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
    #創建資料庫對話
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    #創建base
    Base = declarative_base()
    
    Base.metdata.create_all(bind=engine)
    