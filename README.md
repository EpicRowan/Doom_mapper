![Doom Logo](/static/img/Doom_logo.gif)

Doom Mapper is a full stack Web application that allows users to check if a building in San Francisco is in danger of collapse in a 7.0 or higher earthquake.

The application has 93% test coverage using Python unittest.

This project was made at Hackbright Academy in San Francisco over four weeks in February 2020.

### Contents

* [Tech stack](#techstack)
* [Installation](#installation)
* [Features](#features)
* [About The Developer](#aboutme)

## <a name="techstack"></a>Technologies

Tech Stack: Python, JavaScript, HTML, CSS, Flask, Jinja, jQuery, PostgreSQL, SQLAlchemy, Bootstrap, unittest <br>
APIs: Google Maps JavaScript, Google Maps Geocoding

### Prerequisites

- PostgreSQL
- Python 3.x
- API key for Google Maps JavaScript and Google Maps Geocoding

### Run on your local computer

Clone or fork repository:
```
$ git clone https://github.com/teganbroderick/Travelmaps
```
Create and activate a virtual environment inside your travelmaps directory:
```
$ virtualenv env
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Add your API key into the header scripts in static/templates/dashboard.html, map.html, profile.html, and share_map.html, eg:
<br><br>
![api](https://raw.githubusercontent.com/teganbroderick/Travelmaps/master/static/img/YOUR_API_KEY.png)

Create database 'travelmaps':
```
$ createdb travelmaps
```
Run model.py interactively in the terminal, and create database tables:
```
$ python3 -i model.py
>>> db.create_all()
>>> quit()
```
Run the app from the command line.
```
$ python server.py
```