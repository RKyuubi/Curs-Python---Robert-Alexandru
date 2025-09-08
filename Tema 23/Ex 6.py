import requests

if __name__ == "__main__":
    try:
        response = requests.get("https://httpbin.org/status/404")
        if response.status_code == 200:
            print("Pagina a fost gasita cu succes")
        else:
            print(f"Eroare: Pagina nu a fost gasita. \nStatus Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"A aparut o eroare: {e}")