# **Doom Mapper**

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

### <a name="installation"></a>Run Doom Mapper on your computer

Clone or fork repository:
```
$ git clone https://https://github.com/EpicRowan/Doom_mapper
```
Create and activate a virtual environment inside your Doom Mapper directory:
```
$ virtualenv env
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Add your API key into the header scripts templates/homepage.html line 79

Create database 'buildings':
```
$ createdb buildings
```
Run model.py interactively in the terminal, and create database tables:
```
$ python3 -i model.py
>>> db.create_all()
>>> quit()

```
Run seed.py to load all of the data into the newly created and setup database
```
$ python3 seed.py
```
Run the app from the command line.
```
$ python3 server.py
```

## <a name="features"></a>Features

### **Search**
<img src="/static/img/Doom_logo.gif" width="1000" height="200">

#### Search for an address in San Francisco to learn about the seismic risks facing it. If the building is in the database as soft story building or a skyscraper, it will return info about the liquefaction risk, any known flawed construction used, and if the building has been seismically retrofitted.

<img src="/static/img/Results_page.png">

### **Mouse Over Information**

#### Not sure what liquefaction is? Mouseover to learn about the different doom categories and why they are concerning

<img src="/static/img/help_tips.gif" width="1000" height="500">

### **Interactive Map**

#### Red and blue markers indicate different types of buildings and the grey layer indicates the liquefaction zone. They can be toggled on and off. 

<img src="/static/img/Toggle.gif" width="1000" height="500">

### **Browse Soft Story Buildings and Skyscrapers**

#### Mouseover the red or blue markers to see the address or name of the building and click to view the buildings information page. Doom score is calculated based on the known risk factors

### **Bonus Scary Earthquake facts**

Want to be scared off from ever taking an elevator in San Francisco again? How about petrified from long you will be estimated to be without water when the Big One hits? Each page contains a randomly chosen scary fact from the US Geological Survey's estimations of the effects of a 7.0 quake from the Hayward fault.

## <a name="aboutme"></a>About the Developer

 Doom Mapper was created by former teacher Rowan Shepherd, a science and dark humor enthusiast who transitioned into software engineering. This is her first fullstack project. She can be found on [LinkedIn](https://https://www.linkedin.com/in/rowan-shepherd/) and on [Github](https://github.com/EpicRowan).