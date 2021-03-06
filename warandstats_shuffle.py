#ilovetacos
#by @fatcat2
import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
#NEW STATS LISTS
deck1Stats = []
deck2Stats = []
numTurns = []
#create deck variables
masterDeck = []
deck1 = []
deck2 = []
warSpoilsList = []
deck1sum = 0
deck2sum = 0
winnerInt = 0
initialDeckDiff = 0
#initialize face card dictionaries
faceCardDict = {
	11 : "J",
	12 : "Q",
	13 : "K",
	14 : "A"
}

#METHODS
def main():
	#initialize master Deck
	#use try-except to make sure there are less than 53 cards in play
	try:
		numCards = input("How many cards would you like to play with?\n")
		print("------------------------")
		fillMasterDeck(numCards)
	except IndexError:
		print("Please enter a number under 53")
	deal()
	print("COLLECTING DATA")
	play(1)
	winner()
	print("Deck 1 Initial Sum: %i" % deck1sum)
	print("Deck 2 Initial Sum: %i" % deck2sum)
	print("The difference between the initial sums is %i" % abs(deck1sum-deck2sum))
	if(deck1sum > deck2sum):
		print("I predict that Player 1 will win")
	elif(deck2sum > deck1sum):
		print("I predict that Playser 2 will win")
	else:
		print("It's equal - shit gonna go down!!!")
	raw_input("DATA COLLECTION COMPLETE\nPRESS ENTER TO INITIATE DATA ANALYSIS")
	print("Deck %i won" % winnerInt)
	plotThisShit()
	
def fillMasterDeck(numCards):
	#Thanks to /u/SmartAsFart for these optimizations!
	global masterDeck
	pool = [x for x in range(2, 15)]*4
	masterDeck += [pool.pop(random.randrange(0, len(pool))) for i in range(numCards)]

def deal():
	turndicator = True
	deckLen = len(masterDeck)
	for x in range(0, deckLen):
		popCard = masterDeck.pop(random.randint(0, len(masterDeck)-1))
		if(turndicator):
			deck1.append(popCard);
			turndicator = not turndicator
		else:
			deck2.append(popCard);
			turndicator = not turndicator
	global deck1sum
	global deck2sum
	deck1sum = sum(deck1)
	deck2sum = sum(deck2)

def play(turn_counter):
	if(turn_counter%10 == 0):
		random.shuffle(deck1)
		random.shuffle(deck2)
	deck1Len = len(deck1)
	deck2Len = len(deck2)
	deck1Stats.append(deck1Len)
	deck2Stats.append(deck2Len)
	numTurns.append(turn_counter)
	if(len(deck1) == 0 or len(deck2) == 0):
		pass;
	else:
		card1 = deck1.pop(0)
		card2 = deck2.pop(0)
		if(card1 > card2 or card2 > card1):
			battle(card1, card2, False)
		elif(card1 == card2):
			war(card1, card2)
		turn_counter += 1
		play(turn_counter)

def war(card1, card2):
	warSpoilsList.extend([card1, card2])
	if(len(deck1) == 0 or len(deck2) == 0):
		pass
	else:
		card1 = deck1.pop(0)
		card2 = deck2.pop(0)
		if(card1 > card2 or card2 > card1):
			battle(card1, card2, True)
		elif(card1 == card2):
			war(card1, card2)

def battle(card1, card2, isWar):
	if(card1 > card2):
		deck1.append(card1)
		deck1.append(card2)
		if(not isWar):
			pass
		else:
			warSpoils(True)
	elif(card1 < card2):
		deck2.append(card1)
		deck2.append(card2)
		if(not isWar):
			pass
		else:
			warSpoils(False)

def winner():
	global winnerInt
	if(len(deck1) == 0):
		print("Player 2 Wins!!!")
		winnerInt = 2
	else:
		print('Player 1 Wins!!!')
		winnerInt = 1

def warSpoils(deck1win):
	if(deck1win):
		warSpoilsList.append(deck2.pop(0))
		deck1.extend(warSpoilsList)
	elif(not deck1win):
		warSpoilsList.append(deck1.pop(0))
		deck2.extend(warSpoilsList)
	del warSpoilsList[:]

def plotThisShit():
	plt.xkcd()
	plt.plot(numTurns, deck1Stats, color="r")
	plt.plot(numTurns, deck2Stats, color="b")
	plot_title = "Amount of cards in each deck in a simulated game of war over %i turns" % numTurns[len(numTurns)-1]
	plt.title(plot_title)
	plt.xlabel("Turn Number")
	plt.ylabel("Amount of Cards in Deck")
	red_patch = mpatches.Patch(color='red', label='Player 1')
	blue_patch = mpatches.Patch(color='blue', label="Player 2")
	plt.legend(handles=[red_patch, blue_patch])
	plt.show()

if __name__ == "__main__": main()