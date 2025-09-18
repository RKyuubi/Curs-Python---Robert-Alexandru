import csv
from fastapi import FastAPI, HTTPException, APIRouter
from typing import List, Optional

router = APIRouter(prefix="/order", tags=["food order"])

def read_menu_from_csv():
    try:
        with open('db/Restaurant Menu.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Menu file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading menu file: {str(e)}")

@router.get("/menu/search", response_model=Optional[dict])
def search_item(name: str):
    """Căutare după numele produsului, returnând toate detaliile."""
    menu_data = read_menu_from_csv()
    found_item = next((item for item in menu_data if name.lower() in item['name'].lower()), None)

    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")

    return found_item

@router.post("/orders/{item_id}", status_code=201)
def place_order(item_id: int):
    """Plasează o comandă pentru un produs după ID."""
    menu_data = read_menu_from_csv()
    item = next((item for item in menu_data if int(item['id']) == item_id), None)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found in the menu")

    return {"message": f"Successfully placed an order for {item['name']}"}