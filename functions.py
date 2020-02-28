
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
		facts = ["It is thought that more damage was done by the resulting fire after the 1906 \
		San Francisco earthquake than by the earthquake itself.", "It is predicted that if the Big One hits San Francisco during the day, upwards of \
		1,000 people might be trapped in elevators alone", ]

		return random.choice(facts)