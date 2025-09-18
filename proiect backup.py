import csv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


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


def read_menu_from_csv():
    try:
        with open('db/Restaurant Menu.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Menu file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading menu file: {str(e)}")


@app.get("/menu", response_model=dict)
def get_full_menu():
    """Returnează meniul complet, organizat pe categorii."""
    menu_data = read_menu_from_csv()
    starters = [item for item in menu_data if item['category'] == 'starters']
    main_courses = [item for item in menu_data if item['category'] == 'main_course']
    deserts = [item for item in menu_data if item['category'] == 'deserts']

    return {
        "starters": starters,
        "main_courses": main_courses,
        "deserts": deserts
    }


@app.get("/menu/starters", response_model=List[Starter])
def get_starters():
    """Returnează doar antreurile (Starters)."""
    menu_data = read_menu_from_csv()
    starters = [
        Starter(
            id=int(item['id']),
            name=item['name'],
            price=float(item['price']),
            description=item['description']
        )
        for item in menu_data if item['category'] == 'starters'
    ]
    return starters


@app.get("/menu/main_course", response_model=List[MainCourse])
def get_main_courses():
    """Returnează doar felurile principale (Main Course)."""
    menu_data = read_menu_from_csv()
    main_courses = [
        MainCourse(
            id=int(item['id']),
            name=item['name'],
            price=float(item['price']),
            description=item['description']
        )
        for item in menu_data if item['category'] == 'main_course'
    ]
    return main_courses


@app.get("/menu/deserts", response_model=List[Desert])
def get_deserts():
    """Returnează doar deserturile (Deserts)."""
    menu_data = read_menu_from_csv()
    deserts = [
        Desert(
            id=int(item['id']),
            name=item['name'],
            price=float(item['price']),
            description=item['description']
        )
        for item in menu_data if item['category'] == 'deserts'
    ]
    return deserts


@app.get("/menu/search", response_model=Optional[dict])
def search_item(name: str):
    """Căutare după numele produsului, returnând toate detaliile."""
    menu_data = read_menu_from_csv()
    found_item = next((item for item in menu_data if name.lower() in item['name'].lower()), None)

    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")

    return found_item

@app.post("/orders/{item_id}", status_code=201)
def place_order(item_id: int):
    """Plasează o comandă pentru un produs după ID."""
    menu_data = read_menu_from_csv()
    item = next((item for item in menu_data if int(item['id']) == item_id), None)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found in the menu")

    return {"message": f"Successfully placed an order for {item['name']}"}