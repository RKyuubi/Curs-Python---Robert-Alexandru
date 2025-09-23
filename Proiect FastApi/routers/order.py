from fastapi import APIRouter, HTTPException, status
from .functii import read_menu_from_csv, write_menu_to_csv, get_sold_count
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

@router.get("/menu/top_sold_by_category", response_model=dict)
def get_top_sold_by_category():
    """Returnează cel mai vândut fel de mâncare din fiecare categorie."""
    menu_data = read_menu_from_csv()
    top_items_by_category = {}
    categories = ['starters', 'main_course', 'deserts']

    for category in categories:
        category_items = [item for item in menu_data if item['category'] == category]
        if not category_items:
            continue

        try:
            sorted_items = sorted(category_items, key=get_sold_count, reverse=True)
            top_item = sorted_items[0]

            top_items_by_category[category] = {
                'name': top_item['name'],
                'price': float(top_item['price']),
                'description': top_item['description']
            }
        except (ValueError, TypeError):
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Invalid data in sold_count field for category {category}")

    return top_items_by_category