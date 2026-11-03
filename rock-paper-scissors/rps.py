										##############################
  										#  Rock - Papers - Scissors  #
										##############################
import random
options = ("ROCK", "PAPER", "SCISSOR")
Beats = {"ROCK" : "PAPER", "PAPER" : "SCISSOR","SCISSOR" : "ROCK"}
draws = {"ROCK":"ROCK","PAPER":"PAPER","SCISSOR":"SCISSOR"}
userWins , computerWins ,playing = 0, 0 , True
while playing:
	print("##############################")
	print("#  Rock - Papers - Scissors  #")
	print("##############################")
	userChoice = input("Choose your option: ").upper()
	while userChoice not in options:
		userChoice = input("Invalid choice - choose Again ").upper()
	computerChoice = random.choice(options)
	print(f"your choice is {userChoice} VS Computer_Choice is {computerChoice}")
	if (userChoice, computerChoice) in Beats.items():
		print("Sorry!! computer wins")
		computerWins += 1
	elif (userChoice, computerChoice) in draws.items():
		print("its a Tie")
	else:
		print("congratulations!!!you win")
		userWins += 1
	print("########################################################")
	print(f"\tuserWins : {userWins} //  computerWins : {computerWins}")
	print("########################################################")
	Play_Again = input("Do you want to play again? (y/n) ").lower()
	if Play_Again == "n":
		playing = False
		print(
			f"the FINAL_SCORE is :\nuserWins : {userWins} and computerWins : {computerWins} \n \t\tTHANK YOU SEE YOU SOON")

