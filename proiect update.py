import csv
from fastapi import FastAPI, HTTPException, status
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

def read_menu_from_csv():
    try:
        with open('Proiect FastApi/db/Restaurant Menu.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Menu file not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error reading menu file: {str(e)}")


def write_menu_to_csv(menu_data):
    try:
        fieldnames = ['id', 'category', 'name', 'price', 'description', 'sold_count']
        with open('Proiect FastApi/db/Restaurant Menu.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(menu_data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error writing to menu file: {str(e)}")


def read_users_from_csv():
    try:
        with open('Proiect FastApi/db/users.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Users file not found")


def authenticate_user(username: str, password: str):
    users = read_users_from_csv()
    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    return user

def get_next_id():
    menu_data = read_menu_from_csv()
    if not menu_data:
        return 1
    max_id = max(int(item['id']) for item in menu_data)
    return max_id + 1

@app.get("/menu", response_model=dict)
def get_full_menu():
    """Returnează meniul complet, organizat pe categorii."""
    menu_data = read_menu_from_csv()
    starters = [
        {k: v for k, v in item.items() if k not in ['id', 'category', 'sold_count']}
        for item in menu_data if item['category'] == 'starters'
    ]
    main_courses = [
        {k: v for k, v in item.items() if k not in ['id', 'category', 'sold_count']}
        for item in menu_data if item['category'] == 'main_course'
    ]
    deserts = [
        {k: v for k, v in item.items() if k not in ['id', 'category', 'sold_count']}
        for item in menu_data if item['category'] == 'deserts'
    ]
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
        Starter(id=int(item['id']), name=item['name'], price=float(item['price']), description=item['description'])
        for item in menu_data if item['category'] == 'starters'
    ]
    for starter in starters:
        del starter.id
    return starters


@app.get("/menu/main_course", response_model=List[MainCourse])
def get_main_courses():
    """Returnează doar felurile principale (Main Course)."""
    menu_data = read_menu_from_csv()
    main_courses = [
        MainCourse(id=int(item['id']), name=item['name'], price=float(item['price']), description=item['description'])
        for item in menu_data if item['category'] == 'main_course'
    ]
    for course in main_courses:
        del course.id
    return main_courses


@app.get("/menu/deserts", response_model=List[Desert])
def get_deserts():
    """Returnează doar deserturile (Deserts)."""
    menu_data = read_menu_from_csv()
    deserts = [
        Desert(id=int(item['id']), name=item['name'], price=float(item['price']), description=item['description'])
        for item in menu_data if item['category'] == 'deserts'
    ]
    for desert in deserts:
        del desert.id
    return deserts


@app.get("/menu/search", response_model=Optional[dict])
def search_item(name: str):
    """Căutare după numele produsului, returnând toate detaliile."""
    menu_data = read_menu_from_csv()
    found_item = next((item for item in menu_data if name.lower() in item['name'].lower()), None)
    if not found_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {k: v for k, v in found_item.items() if k not in ['id', 'sold_count']}


@app.post("/menu/add", status_code=status.HTTP_201_CREATED)
def add_item_to_menu(
        item: MenuItem,
        username: str,
        password: str
):
    authenticate_user(username, password)
    menu_data = read_menu_from_csv()
    new_id = get_next_id()

    new_item = item.model_dump()
    new_item['id'] = str(new_id)
    new_item['price'] = f"{new_item['price']:.2f}"
    new_item['sold_count'] = str(new_item['sold_count'])

    menu_data.append(new_item)
    write_menu_to_csv(menu_data)
    return {"message": "Item added successfully"}


@app.post("/orders/item name", status_code=status.HTTP_201_CREATED)
def place_order(order: OrderRequest):
    """Plasează o comandă pentru unul sau mai multe produse specificate după nume."""
    menu_data = read_menu_from_csv()
    ordered_items = []

    for item_name in order.items:
        found_item = next((item for item in menu_data if item['name'].lower() == item_name.lower()), None)
        if not found_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item not found: {item_name}")

        ordered_items.append(found_item)

    for item in ordered_items:
        item['sold_count'] = str(int(item.get('sold_count', 0)) + 1)

    write_menu_to_csv(menu_data)

    return {"message": "Order placed successfully", "ordered_items": [item['name'] for item in ordered_items]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)