

from jinja2 import StrictUndefined
from sqlalchemy import func, or_

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Building, SoftStory, TallBuilding
from functions import get_doom, random_fact
import json


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# # Normally, if you use an undefined variable in Jinja2, it fails silently.
# # This is horrible. Fix this so that, instead, it raises an error.

app.jinja_env.undefined = StrictUndefined



@app.route('/')
def view_home_map():

    """Renders the main homepage, main Google Map with clickable markers on map, and search feature"""


    return render_template("homepage.html")


@app.route("/api/tallbuildings")
def building_info():

    """JSON information about tall buildings to be used in the blue markers on the Google Maps API"""


    tallbuildings = [
{
    "id": tallbuilding.building_id,
    "name": tallbuilding.name,
    "liquefaction": tallbuilding.liquefaction,
    "at_risk": tallbuilding.at_risk,
    "latitude": tallbuilding.building.latitude,
    "longitude": tallbuilding.building.longitude,
    "address": tallbuilding.building.address,


}
    for tallbuilding in TallBuilding.query.all()
]

    return jsonify(tallbuildings)

@app.route("/api/softbuildings")
def softstory_info():

    """JSON information about soft story buildings to be used in the red markers on the Google Maps API"""

    softbuildings = [
{
    "id": softstory.building_id,
    "status": softstory.status,
    "address": softstory.building.address,
    "latitude": softstory.building.latitude,
    "longitude": softstory.building.longitude


}
    for softstory in SoftStory.query.all()
]

    return jsonify(softbuildings)



@app.route("/buildings/<id>")
def display(id):

    """Enables clicking on a marker and retrieving the information about that location, either soft story or tall building, on the search results page"""

    searched = Building.query.get(id)

    doom = get_doom(searched)

    fact = random_fact()

    return render_template("building_details.html", searched=searched, doom=doom, fact=fact)



@app.route("/search")
def search_results():

    """Search for an address that in the database as either a softstory or tall building in San Francisco and show the data on the search results page""" 

    find_address = request.args.get("entered_address")

    #Makes the search case insenstitive 

    count_search = Building.query.filter(Building.address.ilike (find_address + "%"),).count()

    fact = random_fact()

    if count_search > 1:

        return render_template ("multiple_results.html", count_search = count_search, fact=fact)

    else:
    
        searched = Building.query.filter(Building.address.ilike (find_address + "%"),).first()
   
    #if there is no record in the database, return the Not Found page

    if searched == None:

        return render_template("not_found_results.html", find_address=find_address, fact=fact)

    else:

        doom = get_doom(searched)


        return render_template("building_details.html", searched=searched, doom=doom, fact=fact)



if __name__ == "__main__": # pragma: no cover
# We have to set debug=True here, since it has to be True at the point
# that we invoke the DebugToolbarExtension
    # app.debug = True

    connect_to_db(app)

    #Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")




