from pydantic import BaseModel

class Starter(BaseModel):
    id: int
    name: str
    price: float
    description: str


class MainCourse(BaseModel):
    id: int
    name: str
    price: float
    description: str


class Desert(BaseModel):
    id: int
    name: str
    price: float
    description: str