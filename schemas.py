from pydantic import BaseModel

class Insertt(BaseModel):
    s_id: int
    s_name: str
    s_marks: int
    s_result: str

class Supdate(BaseModel):
    s_name: str
    s_marks: int
    s_result: str