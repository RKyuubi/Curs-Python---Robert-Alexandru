import requests

if __name__ == "__main__":
    try:
        response = requests.get("https://httpbin.org/image/png")
        with open("imagine.png", "wb") as file:
            file.write(response.content)

        print(f"Imaginea a fost descarcata si salvata ca '{"imagine.png"}'")

    except requests.exceptions.RequestException as e:
        print(e)


