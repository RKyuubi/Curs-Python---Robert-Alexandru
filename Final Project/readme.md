# 🐞 Bug Tracker Flask & SocketIO

Un sistem modern de gestionare a bug-urilor construit cu Flask (Python), MySQL și SocketIO pentru comunicare în timp real.

## 1. Descriere Generală Proiect 

### Scopul Proiectului

Scopul principal al aplicației este de a oferi o platformă centralizată și în timp real pentru gestionarea ciclului de viață al tichetelor. Aplicația facilitează colaborarea între membrii echipei (Admini, Reporteri și Developeri) prin sincronizarea imediată a schimbărilor.

### Funcționalități Cheie

| Modul | Descriere |
| :--- | :--- |
| **Autentificare bazată pe Roluri** | Utilizatori cu roluri de **Admin**, **Reporter** și **Developer** (implementat cu `Flask-Login`). |
| **Gestionarea Tichetelor (CRUD)** | Crearea, vizualizarea și ștergerea tichetelor. Ștergerea este restricționată la Reporterul original al tichetului sau la Admin. |
| **Comentarii în Timp Real** | Adăugarea de comentarii la tichete, sincronizate instantaneu prin **SocketIO**. |
| **Sincronizare Instantanee** | Toate acțiunile critice (creare/ștergere tichet, adăugare comentariu) declanșează evenimente SocketIO pentru a actualiza interfața tuturor utilizatorilor conectați. |
| **Integritate a Datelor** | Implementarea **Cascade Delete** în SQLAlchemy (`models.py`) pentru a asigura ștergerea automată a comentariilor asociate la ștergerea unui tichet. |

---

## 2. Instrucțiuni Clare de Instalare și Rulare

### 2.1. Cerințe Preliminare

1.  **Python 3.8+**
2.  **MySQL Server** (pornit și accesibil)

### 2.2. Instalarea Dependențelor

**Pasul 1: Clonarea proiectului**

git clone <URL-ul_repozitoriului_tau>
cd bugtracker

**Pasul 2: Clonarea proiectului**

***Creează mediul virtual***

- python -m venv .venv

***Activează mediul virtual (Windows)***
- .venv\Scripts\activate

***Activează mediul virtual (macOS/Linux)***
- source .venv/bin/activate

**Pasul 3: Instalarea Pachetului Python**

pip install -r requirements.txt

### 2.3. Configurarea Bazei de Date și Variabile de Mediu
1. Creați Baza de Date: În clientul MySQL (Workbench, CLI, etc.), creați baza de date: CREATE DATABASE bugtracker;
2. Verificați fișierul .env: Asigurați-vă că detaliile de conexiune se potrivesc cu configurarea locală MySQL.

### 2.4. Rularea Aplicației
Aplicația este rulată direct prin scriptul app.py, care inițializează serverul Flask și SocketIO: python app.py

Serverul va porni la adresa: http://127.0.0.1:5000/

Notă la Prima Rulare: 
- Scriptul app.py va apela db.create_all() pentru a crea tabelele.
- Funcția seed_data(app) va crea conturile de test și tichetele inițiale (dacă baza de date este goală).

Conturi de Test (Seed Data)Folosiți aceste credențiale pentru a testa diferitele roluri:

Utilizator,Parolă,Rol

- Robert_Alexandru,admin_password,Admin
- Ana_Tester,tester_password,Reporter
- Vlad_Dev,dev_password,Developer
