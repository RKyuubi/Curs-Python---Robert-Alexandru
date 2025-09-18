import csv
from fastapi import FastAPI, HTTPException, APIRouter
from typing import List, Optional
from models import Starter, MainCourse

router = APIRouter(prefix="/food", tags=["food"])

def read_menu_from_csv():
    try:
        with open('db/Restaurant Menu.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Menu file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading menu file: {str(e)}")


@router.get("/menu", response_model=dict)
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


@router.get("/menu/starters", response_model=List[Starter])
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


@router.get("/menu/main_course", response_model=List[MainCourse])
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