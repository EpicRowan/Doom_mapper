
import random 


def get_doom(building):

	doom_score = 0

	doom_rating = {0: "Probaby Not Doomed!", 1: "Low chance of Doom", 2: "Low chance of Doom", \
				3: "Possibly Doomed", 4: "Possibly Doomed", 5: "Moderately Doomed", 6: "Probaby Doomed", \
				7: "Very Likely Doomed", 8: "Super high chance of Doom", 9: "Extremely High chance of Doom!", 10: "Doom is Almost Guaranteed!" } \

	if building.softstory:

		if building.softstory.status == "Non-Compliant":

			doom_score += 5

	elif building.tallbuilding:
		if building.tallbuilding.at_risk == True:
			doom_score += 5

		if building.tallbuilding.liquefaction == "Very High":
			doom_score += 5
			
		elif building.tallbuilding.liquefaction == "High":
			doom_score += 4

		elif building.tallbuilding.liquefaction == "Moderate":
			doom_score += 3

		elif building.tallbuilding.liquefaction == "Low":
			doom_score += 2

	return doom_rating[doom_score]



def random_fact():
		facts = ["It is predicted that if the Big One hits San Francisco during the day, upwards of \
		22,000 people might be trapped in approximately 4,600 stalled elevators.", "Estimates show that after a 7.0+, most people will \
		be without running water for approximately six weeks but some will be without water for up to six months", \
		"Charles Richter, creator of the Richter scale, said about skyscrapers 'Don’t build them in California.'", \
		"It is estimated that a 7.0+ quake from the Hayward fault will trap about 2,500 people in around 5,000 collapsed buildings", \
		"A large earthquake from the Hayward fault is predicted to spark as many as 670 fires, approximately 450 of which \
		could not be easily contained." , "While most earthquakes last only 10 to 30 seconds, occasscionally the shaking lasts for up \
		to ten minutes.", "Due to the over 1,000 miles of old sewer systems under San Francisco, a large quake will likely \
		cause numerous sinkholes large enough to swallow cars or even whole buildings." 

		]

		return random.choice(facts)