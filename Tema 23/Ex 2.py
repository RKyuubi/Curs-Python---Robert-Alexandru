import requests

if __name__ == "__main__":
    parametrii = {"name": "Ion", "varsta": 25}
    try:
        response = requests.get("https://httpbin.org/get", params=parametrii)
        print(f"Raspunsul in format JSON: \n{response.json()}")

    except requests.exceptions.RequestException as e:
        print(f"A aparut o eroare: {e}")