import csv
from fastapi import HTTPException, status

def read_menu_from_csv():
    try:
        with open('db/Restaurant Menu.csv', mode='r', encoding='utf-8') as file:
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
        with open('db/Restaurant Menu.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(menu_data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error writing to menu file: {str(e)}")


def read_users_from_csv():
    try:
        with open('db/users.csv', mode='r', encoding='utf-8') as file:
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

def get_sold_count(item):
    return int(item.get('sold_count', 0))