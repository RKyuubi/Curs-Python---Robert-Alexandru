import csv
from fastapi import FastAPI, HTTPException, APIRouter
from typing import List, Optional
from models import Desert

router = APIRouter(prefix="/desert", tags=["deserts"])

def read_menu_from_csv():
    try:
        with open('db/Restaurant Menu.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Menu file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading menu file: {str(e)}")

@router.get("/menu/deserts", response_model=List[Desert])
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