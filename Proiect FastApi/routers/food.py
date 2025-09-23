from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from models import Starter, MainCourse, Desert, MenuItem
from .functii import read_menu_from_csv, write_menu_to_csv, authenticate_user, get_next_id

router = APIRouter()

@router.get("/menu", response_model=dict)
def get_full_menu():
    """Returnează meniul complet, organizat pe categorii."""
    menu_data = read_menu_from_csv()
    starters = [
        Starter(id=int(item['id']), name=item['name'], price=float(item['price']), description=item['description'])
        for item in menu_data if item['category'] == 'starters']

    main_courses = [
        MainCourse(id=int(item['id']), name=item['name'], price=float(item['price']), description=item['description'])
        for item in menu_data if item['category'] == 'main_course'
    ]

    deserts = [
        Desert(id=int(item['id']), name=item['name'], price=float(item['price']), description=item['description'])
        for item in menu_data if item['category'] == 'deserts'
    ]
    for starter in starters:
        del starter.id
    for main_course in main_courses:
        del main_course.id
    for desert in deserts:
        del desert.id
    return {
        "starters": starters,
        "main_courses": main_courses,
        "deserts": deserts
    }


@router.get("/menu/starters", response_model=List[Starter])
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


@router.get("/menu/main_course", response_model=List[MainCourse])
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


@router.get("/menu/deserts", response_model=List[Desert])
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


@router.get("/menu/search", response_model=Optional[dict])
def search_item(name: str):
    """Căutare după numele produsului, returnând toate detaliile."""
    menu_data = read_menu_from_csv()
    found_item = next((item for item in menu_data if name.lower() in item['name'].lower()), None)
    if not found_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {k: v for k, v in found_item.items() if k not in ['id', 'sold_count']}


@router.post("/menu/add", status_code=status.HTTP_201_CREATED)
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