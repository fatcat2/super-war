#ilovetacos
#by @fatcat2
import random

#create deck variables
masterDeck = []
deck1 = []
deck2 = []

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
		print(numCards)
		fillMasterDeck(numCards)
	except IndexError:
		print("Please enter a number under 53")

	#initialize player decks
	deal()
	# play()
	recursive_play(1)
	winner()
	
def fillMasterDeck(numCards):
	#Jack = 11
	#Queen = 12
	#King = 13
	#Ace = 14
	pool = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14]
	poolsize = len(pool)
	# print("yes")
	for x in range(0, numCards):
		masterDeck.append(pool.pop(random.randint(0, len(pool))))
	print("Master Deck Cards:")
	print masterDeck

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

def recursive_play(turn_counter):
	print "Turn %i" % turn_counter
	if(len(deck1) == 0 or len(deck2) == 0):
		pass;
	else:
		print "Player 1 has %i cards" % len(deck1)
		print "Player 2 has %i cards" % len(deck2)
		card1 = deck1.pop(0)
		printDrawnCard("Player 1", card1)
		card2 = deck2.pop(0)
		printDrawnCard("Player 2", card2)
		if(card1 > card2 or card2 > card1):
			battle(card1, card2, False)
		elif(card1 == card2):
			war()
		turn_counter += 1
		print("\n")
		next = input("press enter to proceed")
		print next
		recursive_play(turn_counter)

def play():
	turn_counter = 0
	while(len(deck1) > 0 and len(deck2) > 0):
		turn_counter += 1
		print "Turn %i" % turn_counter
		print "Player 1 has %i cards" % len(deck1)
		print "Player 2 has %i cards" % len(deck2)
		card1 = deck1.pop(0)
		printDrawnCard("Player 1", card1)
		card2 = deck2.pop(0)
		printDrawnCard("Player 2", card2)
		if(card1 > card2 or card2 > card1):
			battle(card1, card2, False)
		elif(card1 == card2):
			war()

		next_turn = raw_input("Press Enter to proceed\n")

def war():
	print "WAR!"
	print len(deck1)
	print len(deck2)
	print "Player 1 has %i cards" % len(deck1)
	print "Player 2 has %i cards" % len(deck2)
	#Formatting for card
	#!!!PLEASE COMPARTMENTALIZE FORMATTING IN A METHOD!!!
	card1 = deck1.pop(0)
	printDrawnCard("Player 1", card1)
	card2 = deck2.pop(0)
	printDrawnCard("Player 2", card2)
	if(card1 > card2 or card2 > card1):
		battle(card1, card2, True)
	elif(card1 == card2):
		war()

def battle(card1, card2, isWar):
	if(card1 > card2):
		deck1.append(card1)
		deck1.append(card2)
		print "Player 1 gained a %i and a %i" % (card1, card2)
		print "Player 1 has %i cards" % len(deck1)
		print "Player 2 has %i cards" % len(deck2)
		try:
			warSpoils(isWar, True)
		except IndexError:
			pass
	elif(card1 < card2):
		deck2.append(card1)
		deck2.append(card2)
		print "Player 2 gained a %i and a %i" % (card1, card2)
		print "Player 1 has %i cards" % len(deck1)
		print "Player 2 has %i cards" % len(deck2)
		try:
			warSpoils(isWar, True)
		except IndexError:
			pass
		print "Player 2 gained a %i and a %i" % (card1, card2)

def winner():
	print "Player 1 has %i cards" % len(deck1)
	print "Player 2 has %i cards" % len(deck2)
	if(len(deck1) == 0):
		print "Player 2 Wins!!!"
	else:
		print 'Player 1 Wins!!!'

def draw():
	return deck.pop(0)

def printDrawnCard(playerName, card):
	if(card > 10):
		print "%s drew a %s" % (playerName, faceCardDict[card])
	else:
		print "%s drew a %i" % (playerName, card)

def warSpoils(iswar, deck1win):
	if(deck1win and iswar):
		deck1.append(deck2.pop(0))
	elif(not deck1win and iswar):
		deck2.append(deck1.pop(0))















if __name__ == "__main__": main()