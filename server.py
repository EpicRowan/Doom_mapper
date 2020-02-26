

from jinja2 import StrictUndefined
from sqlalchemy import func, or_

from flask import Flask, render_template, request, flash, redirect, session, jsonify
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
def view_home_map():

    """Homepage and main Google Map with clickable markers on map"""

    return render_template("homepage.html")


@app.route("/api/tallbuildings")
def building_info():

    """JSON information about buildings."""


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
    """JSON information about buildings."""


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



# @app.route("/buildings/search")
# def display(address):

#     searched = Building.query.get(address)

#     return render_template("search.html", searched = searched )



@app.route("/search")
def search_results():

	'''Search for an address that is in the database as either a softstory or tall building in San Francisco and retrieve the data''' 
	
	searched = request.args.get("entered_address")

	#Makes the search case insenstitive 

	find_building = Building.query.filter(Building.address.ilike (searched + "%"),).first()



	#if there is no record in the database, return the Not Found page

	if find_building == None:
    
    
		return render_template("not_found_results.html")


	#if it is in the tall buildings csv file

	if find_building.tallbuilding:

		liquefaction = find_building.tallbuilding.liquefaction

		at_risk = find_building.tallbuilding.at_risk

		score = doom_score_tall(liquefaction, at_risk)


		return render_template("tallbuilding_results.html", liquefaction=liquefaction, at_risk=at_risk, score=score)

	#if it is in the soft story buildings csv file

	elif find_building.softstory:

		status = find_building.softstory.status

		score = doom_score_soft(status)
	
		return render_template("softstory_results.html", status=status, score=score)

	#catch all for other situations

	else:

		return render_template("not_found_results.html")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
