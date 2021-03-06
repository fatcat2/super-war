#ilovetacos
#by @fatcat2
#python2.7

import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

bigListDeck1 = []
bigListDeck2 = []
bigListNumTurns = []
avgDeck1 = []
avgDeck2 = []
masterDeck = []
masterDeck_master = []
deck1 = []
deck2 = []
warSpoilsList = []
deck1Hand = []
deck2Hand = []
numTurns = []
testNumTurns = 50
faceCardDict = {
	11 : "J",
	12 : "Q",
	13 : "K",
	14 : "A"
}

def main():
	global deck1Hand
	global bigListDeck1
	global bigListDeck2
	global deck2Hand
	global testNumTurns
	#initialize master Deck
	#use try-except to make sure there are less than 53 cards in play
	numCards = int(input("How many cards would you like to play with?\n"))
	print("------------------------\nCollecting Data...")
	while(len(bigListNumTurns) <= 10):
		fillMasterDeck(numCards)
		deal()
		play(1)
		if(len(numTurns) >= testNumTurns):
			bigListDeck1.append(deck1Hand[:])
			bigListDeck2.append(deck2Hand[:])
			bigListNumTurns.append(len(numTurns))
		clearLists()
	raw_input("Data collection complete.\nPress enter to inititate data analysis.")
	lotsOfStats(testNumTurns)
	plotThisShit(testNumTurns)
	print("All done!")
	
def fillMasterDeck(numCards):
	#Thanks to /u/SmartAsFart for these optimizations!
	pool = [x for x in range(2, 15)]*4
	global masterDeck
	masterDeck += [pool.pop(random.randrange(0, len(pool))) for i in range(numCards)]

def deal():
	turndicator = True #indicates whether or not it is Player One's turn to take a card
	deckLen = len(masterDeck) # have this stored as a variable since the masterDeck's length will change as cards get popped
	for x in range(0, deckLen):
		popCard = masterDeck.pop(random.randint(0, len(masterDeck)-1))
		if(turndicator):
			deck1.append(popCard);
			turndicator = not turndicator
		else:
			deck2.append(popCard);
			turndicator = not turndicator

def play(turn_counter):
	numTurns.append(turn_counter)
	deck1Hand.append(len(deck1))
	deck2Hand.append(len(deck2))
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

def warSpoils(deck1win):
	if(deck1win):
		if(len(deck2) != 0):
			warSpoilsList.append(deck2.pop(0))
		deck1.extend(warSpoilsList)
	else:
		if(len(deck1) != 0):
			warSpoilsList.append(deck1.pop(0))
		deck2.extend(warSpoilsList)
	del warSpoilsList[:]

def excelStats():
	wb2 = load_workbook("warstats.xlsx")
	print(wb2.get_sheet_names())

def lotsOfStats(testNumTurns):
	#compute the averages in deck 1 first
	#Computes the average of a turn
	for turn in range(0, testNumTurns):
		avg = 0
		for iteration in range(0, 10):
			avg += bigListDeck1[iteration][turn]
		avg = avg/10.0
		avgDeck1.append(avg)
	for turn in range(0, testNumTurns):
		avg = 0
		for iteration in range(0, 10):
			avg += bigListDeck2[iteration][turn]
		avg = avg/10.0
		avgDeck2.append(avg)

def plotThisShit(testNumTurns):
	plt.xkcd()
	plt.plot(range(0, testNumTurns), avgDeck1, color="r")
	plt.plot(range(0, testNumTurns), avgDeck2, color="b")
	title = "The Average Amount of Cards in a Deck per Turn over %i turns in a Simulated Game of War" % testNumTurns
	plt.title(title)
	plt.xlabel("Turn Number")
	plt.ylabel("Average Amount of Cards in Deck")
	red_patch = mpatches.Patch(color='red', label='Player 1')
	blue_patch = mpatches.Patch(color='blue', label="Player 2")
	plt.legend(handles=[red_patch, blue_patch])
	plt.show()

def clearLists():
	del masterDeck[:]
	del deck1[:]
	del deck2[:]
	del deck1Hand[:]
	del deck2Hand[:]
	del numTurns[:]
if __name__ == "__main__": main()