import random

print("Who do you want to play as? Dwyane Wade, Lebron James, or Steph Curry?")
player = input()
i = 0
if (player == "Dwyane Wade"):
	print("What season do you want to play in? 2005-2006, 2011-2012, or 2012-2013?")
	season = input()
	if (season == "2005-2006"):
		print("Choose a center for your starting lineup: Shaquille O'Neal or Alonzo Mourning")
		center = input()
		if (center == "Shaquille O'Neal"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
		elif(center == "Alonzo Mourning"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(0, 30)
				if (i <= 20):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 21):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
	if(season == "2011-2012"):
		print("Will you be playing Joel Anthony as center? Y/N")
		center = input()
		if (center == "Y"):
			print("Time for tip-off!")
			tip = random.randint(0,3)
			if (tip == 1 or tip == 2):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 3):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
		if(center == "N"):
			print("Time for tip-off!")
			tip = random.randint(0,3)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 2 or tip == 3):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")

	if (season == "2012-2013"):
		print("Are you going to be starting Udonis Haslem or Shane Battier?")
		center = input()
		if (center == "Udonis Haslem"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
		if(center == "Shane Battier"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
if (player == "Lebron James"):
	print("What season do you want to play in? 2011-2012, 2012-2013, or 2015-2016?")
	season = input()
	if(season == "2011-2012"):
		print("Will you be playing Joel Anthony as center? Y/N")
		center = input()
		if (center == "Y"):
			print("Time for tip-off!")
			tip = random.randint(0,3)
			if (tip == 1 or tip == 2):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 3):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
		if(center == "N"):
			print("Time for tip-off!")
			tip = random.randint(0,3)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 2 or tip == 3):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")

	if (season == "2012-2013"):
		print("Are you going to be starting Udonis Haslem or Shane Battier?")
		center = input()
		if (center == "Udonis Haslem"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
		if(center == "Shane Battier"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
	if (season == "2015-2016"):
		print("Choose a center for your starting lineup: Tristan Thompson or Timofey Mozgov")
		center = input()
		if (center == "Tristan Thompson"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
		if(center == "Timofey Mozgov"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(0, 30)
				if (i <= 20):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 21):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")

if (player == "Steph Curry"):
	print("What season do you want to play in? 2014-2015, 2016-2017, or 2017-2018?")
	season = input()
	if(season == "2014-2015"):
		print("Will you allow Kerr to change the team's playstyle to boost Curry? Y/N")
		center = input()
		if (center == "Y"):
			print("Time for tip-off!")
			tip = random.randint(0,3)
			if (tip == 1 or tip == 2):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 3):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
		if(center == "N"):
			print("Time for tip-off!")
			tip = random.randint(0,3)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 2 or tip == 3):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")

	if (season == "2016-2017"):
		print("Will you start Zaza Pachulia as your center? Y/N")
		center = input()
		if (center == "Y"):
			print("Time for tip-off!")
			tip = random.randint(0,3)
			if (tip == 1 or tip == 2):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 3):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 80):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 81):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
		if(center == "N"):
			print("Time for tip-off!")
			tip = random.randint(0,3)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
			if (tip == 2 or tip == 3):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(70, 100)
				if (i <= 90):
					print("You lost the game, sorry!")
					print("You had " + str(i) + " points")
				elif(i >= 91):
					print("You won! Good job!")
					print("You had " + str(i) + " points")
	if (season == "2017-2018"):
		print("Choose a center for your starting lineup: Zaza Pachulia or JaVale McGee")
		center = input()
		if (center == "Zaza Pachulia"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
		if(center == "JaVale McGee"):
			print("Time for tip-off!")
			tip = random.randint(0,2)
			if (tip == 1):
				print("You got the ball! The game is started. How will this game go for you?")
				i = random.randint(0, 30)
				if (i <= 10):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 11):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
			if (tip == 2):
				print("You didn't get the ball. The game is started. Can you make a comeback?")
				i = random.randint(0, 30)
				if (i <= 20):
					print("You lost the game, sorry!")
					print("You had " + str(i+70) + " points")
				elif(i >= 21):
					print("You won! Good job!")
					print("You had " + str(i+70) + " points")
