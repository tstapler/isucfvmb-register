# ISUCF'V'MB Registration App

**Author:** Tyler Stapler

**Description:**  
 This simple Django web app is to facilitate offline registration for the marching band.

## Installation

1. Create a virtual environment to isolate dependencies

```bash
virtualenv env
```

2. Activate the virtual environment

```bash
source env/bin/activate
```

3. Install the requirements

```bash
pip install -r requirements.txt
```

## Use

1. Run the swampdragon websocket server

```bash
python manage.py runsd
```

2. Run the django webserver

```bash
python manage.py runserver
```

3. Navigate to site address
eg: http://localhost:8000

4.
  * The index  located at http://localhost:8000/ is a form to register for band

  * At http://localhost:8000/registered is a live updating list of all the people currently registered

  * Authenticated users can download a .csv file of all students who have registered at http://localhost:8000/registered

## Techs
In this project I used the following tech stack:

* Django backend (Python)
* Swamp Dragon (Websocket Framework for Django)
* Angular Javascript frontend
* Sqlite3 Database for simplicity
* Redis (Required by Swamp Dragon)



