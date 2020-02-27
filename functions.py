

def doom_score_tall(liquefaction, at_risk):

	doom_score = 0


	if liquefaction == "Very High":
			doom_score += 5
			
	elif liquefaction == "High":
			doom_score += 4

	elif liquefaction == "Moderate":
			doom_score += 3

	elif liquefaction == "Low":
			doom_score += 2


	if at_risk == True:
			doom_score += 5


	return doom_score


def doom_score_soft(status):

	doom_score = 0

	#Hoping to find liquefaction data for soft stories in the future


	# if liquefaction == "Very High":
	# 		doom_score += 5
			
	# elif liquefaction == "High":
	# 		doom_score += 4

	# elif liquefaction == "Moderate":
	# 		doom_score += 3

	# elif liquefaction == "Low":
	# 		doom_score += 2


	if status== "Non-Compliant":
			doom_score += 5


	return doom_score


def get_doom(building):

	doom_score = 0

	if building.softstory:

		if building.softstory.status == "Non-Compliant":

			doom_score += 5

	elif building.tallbuilding:

		if building.tallbuilding.liquefaction == "Very High":
			doom_score += 5
			
		elif building.tallbuilding.liquefaction == "High":
			doom_score += 4

		elif building.tallbuilding.liquefaction == "Moderate":
			doom_score += 3

		elif building.tallbuilding.liquefaction == "Low":
			doom_score += 2


	return doom_score