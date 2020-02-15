

from jinja2 import StrictUndefined
from sqlalchemy import func

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Building, SoftStory, TallBuilding
from functions import doom_score_tall,  doom_score_soft

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# # Normally, if you use an undefined variable in Jinja2, it fails silently.
# # This is horrible. Fix this so that, instead, it raises an error.

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def home():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/search")
def search_results():

	
	searched = request.args.get("entered_address")

	find_building = Building.query.filter(Building.address.ilike (searched + "%")).first()



	if find_building == None:

		return render_template("not_found_results.html")

	if find_building.tallbuilding:

		liquefaction = find_building.tallbuilding.liquefaction

		at_risk = find_building.tallbuilding.at_risk

		score = doom_score_tall(liquefaction, at_risk)


		return render_template("tallbuilding_results.html", liquefaction=liquefaction, at_risk=at_risk, score=score)

	elif find_building.softstory:

		status = find_building.softstory.status

		score = doom_score_soft(status)
	
		return render_template("softstory_results.html", status=status, score=score)

	else:

		return render_template("not_found_results.html")


@app.route("/map")
def view_basic_map():
    """Demo of basic map-related code.

    - Programmatically adding markers, info windows, and event handlers to a
      Google Map
    - Showing polylines, directions, etc.
    - Geolocation with HTML5 navigator.geolocate API
    """

    return render_template("map.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
