#ilovetacos
#by @fatcat2
#Python 2.7
import random

#create deck variables
masterDeck = []
deck1 = []
deck2 = []
warSpoilsList = []

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
		numCards = int(raw_input("How many cards would you like to play with?\n"))
		print("------------------------")
		fillMasterDeck(numCards)
	except IndexError:
		print("Please enter a number under 53")

	deal()
	play(1)
	winner()
	
def fillMasterDeck(numCards):
	#Thanks to /u/SmartAsFart for these optimizations!
	raw_input("Press enter to continue")
	pool = [x for x in range(2, 15)]*4
	print(pool)
	global masterDeck
	masterDeck += [pool.pop(random.randrange(0, len(pool))) for i in range(0, numCards)]
	print("Master Deck Cards:")
	print(masterDeck)

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

def play(turn_counter):
	print("--------------------------")
	if(len(deck1) == 0 or len(deck2) == 0):
		pass;
	else:
		print( "Turn %i" % turn_counter)
		print( "Player 1 has %i cards" % len(deck1))
		print( "Player 2 has %i cards" % len(deck2))
		card1 = deck1.pop(0)
		printDrawnCard("Player 1", card1)
		card2 = deck2.pop(0)
		printDrawnCard("Player 2", card2)
		if(card1 > card2 or card2 > card1):
			battle(card1, card2, False)
		elif(card1 == card2):
			war(card1, card2)
		turn_counter += 1
		print("\n")
		raw_input("press enter to proceed")
		play(turn_counter)

def war(card1, card2):
	warSpoilsList.extend([card1, card2])
	print("WAR!")
	if(len(deck1) == 0 or len(deck2) == 0):
		if(len(deck1) == 0):
			print("Player 1 has no cards left")
			pass
		elif(len(deck2) == 0):
			print("Player 2 has no cards left")
			pass
	else:
		card1 = deck1.pop(0)
		printDrawnCard("Player 1", card1)
		card2 = deck2.pop(0)
		printDrawnCard("Player 2", card2)
		if(card1 > card2 or card2 > card1):
			battle(card1, card2, True)
		elif(card1 == card2):
			war(card1, card2)

def battle(card1, card2, isWar):
	if(card1 > card2):
		deck1.append(card1)
		deck1.append(card2)
		print("Player 1 gained a %i and a %i" % (card1, card2))
		print("")
		if(not isWar):
			print("Player 1 has %i cards" % len(deck1))
			print("Player 2 has %i cards" % len(deck2))
		else:
			warSpoils(True)
	elif(card1 < card2):
		deck2.append(card1)
		deck2.append(card2)
		print("Player 2 gained a %i and a %i" % (card1, card2))
		print("")
		if(not isWar):
			print("Player 1 has %i cards" % len(deck1))
			print("Player 2 has %i cards" % len(deck2))
		else:
			warSpoils(False)

def winner():
	print( "Player 1 has %i cards" % len(deck1))
	print( "Player 2 has %i cards" % len(deck2))
	if(len(deck1) == 0):
		print( "Player 2 Wins!!!")
	else:
		print( 'Player 1 Wins!!!')

def printDrawnCard(playerName, card):
	if(card > 10):
		print( "%s drew a %s" % (playerName, faceCardDict[card]))
	else:
		print( "%s drew a %i" % (playerName, card))

def warSpoils(deck1win):
	if(deck1win):
		print( "Player 1 wins the war")
		if(len(deck2) != 0):
			warSpoilsList.append(deck2.pop(0))
		deck1.extend(warSpoilsList)
	else:
		print( "Player 2 wins the war")
		if(len(deck1) != 0):
			warSpoilsList.append(deck1.pop(0))
		deck2.extend(warSpoilsList)
	print("Spoils of War:")
	print(warSpoilsList)
	del warSpoilsList[:]
	print("Player 1 has %i cards" % len(deck1))
	print("Player 2 has %i cards" % len(deck2))



if __name__ == "__main__": main()