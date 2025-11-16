# Folosim cea mai recentă imagine Python subțire (slim), Python 3.13
FROM python:3.13-slim

# Setam directorul de lucru in container
WORKDIR /app

# Copiem fisierul requirements.txt si instalam dependentele
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul codului aplicatiei
COPY . .

# Expunem portul 5000 (standard Flask)
EXPOSE 5000

# Comanda de start pentru aplicatie (folosim gunicorn impreuna cu eventlet pentru suport WebSocket)
CMD exec gunicorn -b :5000 --worker-class sync -w 1 app:app