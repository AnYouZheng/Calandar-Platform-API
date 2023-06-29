from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQL詳細資料
host = ''
user = ''
password = ''
database = ''

class DB_connect:
    SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://user:password@host/database' 
    #定義DB 位址
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    #創建SQLalchmy引擎並連接
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    #創建資料庫對話
    Base = declarative_base()
    #創建base
    Base.metdata.create_all(bind=engine)
    