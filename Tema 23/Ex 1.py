import requests

if __name__ == "__main__":
    try:
        response = requests.get("https://httpbin.org/get")
        print(f"Status Code: {response.status_code}")
        print(f"Primele 200 de caractere din textul raspunsului: \n{response.text[:200]}")

    except requests.exceptions.RequestException as e:
        print(f"A aparut o eroare: {e}")