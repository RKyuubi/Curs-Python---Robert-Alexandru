import requests

if __name__ == "__main__":
    try:
        response = requests.get("https://wttr.in/?format=j1")
        # date_vreme_format_text = response.text
        # print(date_vreme_format_text)  ~~~~~~~ am folosit aceste doua linii pentru a vedea mai bine rezultatul si a-mi da seama cu ce fel de variabile lucrez

        date_vreme = response.json()
        current_weather = date_vreme["current_condition"][0]
        temperature = current_weather["temp_C"]
        weather_description = current_weather["weatherDesc"][0]["value"]

        print (f"Temperatura curenta este: {temperature}C")
        print (f"Conditii de vreme: {weather_description}")

    except requests.exceptions.RequestException as e:
        print(f"A aparut o eroare: {e}")