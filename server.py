

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Building, SoftStory, TallBuilding


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# # Normally, if you use an undefined variable in Jinja2, it fails silently.
# # This is horrible. Fix this so that, instead, it raises an error.
# app.jinja_env.undefined = StrictUndefined


@app.route('/')
def home():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/search")
def search_results():

	searched = request.args.get("entered_address")
	find_building = Building.query.filter(Building.address == searched).first()

	print(find_building)

	# if find_building.tallbuilding == None:

	# 	return render_template("not_found_results.html")

	if find_building.tallbuilding:

		return render_template("tallbuilding_results.html")

	elif find_building.softstory:
		
		return render_template("softstory_results.html")

	else:

		return render_template("not_found_results.html")


    # building = Building.query.get(building_id)
    # return render_template("search_results.html", building=building)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
