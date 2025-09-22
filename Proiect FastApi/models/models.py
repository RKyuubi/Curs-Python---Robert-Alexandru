from pydantic import BaseModel
from typing import List

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


class MenuItem(BaseModel):
    category: str
    name: str
    price: float
    description: str
    sold_count: int


class User(BaseModel):
    username: str
    password: str

class OrderRequest(BaseModel):
    items: List[str]