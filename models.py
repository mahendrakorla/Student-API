from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, INTEGER, VARCHAR
from database import engine

Base = declarative_base()

class Students(Base):
    __tablename__ = "student_data"

    s_id = Column(INTEGER, primary_key=True)
    s_name = Column(VARCHAR(50))
    s_marks = Column(INTEGER)
    s_result = Column(VARCHAR(10))

Base.metadata.create_all(bind=engine)