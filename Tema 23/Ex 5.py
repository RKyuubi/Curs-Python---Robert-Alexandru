import requests

if __name__ == "__main__":
    autentificare = {"utilizator": "admin", "parola": "1234"}
    try:
        response = requests.post("https://httpbin.org/post", params=autentificare, json = "bla bla bla postez orice pe site bla bla bla")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(e)
