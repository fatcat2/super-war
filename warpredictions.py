#ilovetacos
#by @fatcat2
#Python 2.7
import random
import matplotlib.pyplot as plt
#create deck variables
masterDeck = []
deck1 = []
deck2 = []
warSpoilsList = []
deck1sum = 0
deck2sum = 0
winnerInt = 0
initialDeckDiff = 0

predictionList = []

#initialize face card dictionaries
faceCardDict = {
	11 : "J",
	12 : "Q",
	13 : "K",
	14 : "A"
}

#METHODS
def main():
	fillMasterDeck(52)
	for x in range(0, 1000):
		winnerInt = 0
		deal()
		play(1)
		winnerInt = winner()
		greaterInitSum = 0
		if(deck1sum>deck2sum):
			greaterInitSum = 1
		else:
			greaterInitSum = 2
		recordPrediction(greaterInitSum, winnerInt)
	analysis()
	
def fillMasterDeck(numCards):
	pool = [x for x in range(2, 15)]*4
	global masterDeck
	masterDeck += [pool.pop(random.randrange(0, len(pool))) for i in range(0, numCards)]

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
		if(len(deck1) == 0):
			pass
		elif(len(deck2) == 0):
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
		if(isWar):
			warSpoils(True)
			pass
	elif(card1 < card2):
		deck2.append(card1)
		deck2.append(card2)
		if(isWar):
			warSpoils(False)
			pass

def winner():
	if(len(deck1) == 0):
		return 2
	else:
		return 1

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

def recordPrediction(greaterInitSum, winnerInt):
	predictionList.append((greaterInitSum, winnerInt))

def analysis():
	predictRightOn = []
	predictNotRight = []
	for x in predictionList:
		if(x[0] == x[1]):
			predictRightOn.append(x)
		else:
			predictNotRight.append(x)
	plt.xkcd()
	labels = ['Prediction Correct', 'Prediction Incorrect']
	sizes = [(float(len(predictRightOn))/len(predictionList)), (float(len(predictNotRight))/len(predictionList))]
	colors = ['green', 'red']
	explode = [0, 0]
	plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
	plt.axis('equal')
	plt.title('Ratio of Correct Predictions')
	plt.show()



if __name__ == "__main__": main()