from fastapi import APIRouter, HTTPException, status
from .functii import read_menu_from_csv, write_menu_to_csv
from models import OrderRequest

router = APIRouter()

@router.post("/orders/item name", status_code=status.HTTP_201_CREATED)
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