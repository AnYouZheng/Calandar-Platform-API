import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

#從.env 抓出SQL詳細資料
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

# if host == None or user == None or password == None or database == None:
#     print("the variable does not exist or the key is wrong\n")

#定義DB 位址
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8' 

#創建SQLalchemy引擎並連接
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#創建資料庫對話
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#創建base
Base = declarative_base()