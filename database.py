from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MYSQL_user = "root"
MYSQL_pass = "Mahi%404656"
MYSQL_host = "localhost"
MYSQL_port = "3306"
MYSQL_database = "student"

DATABASE_URL = f"mysql+pymysql://{MYSQL_user}:{MYSQL_pass}@{MYSQL_host}:{MYSQL_port}/{MYSQL_database}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()