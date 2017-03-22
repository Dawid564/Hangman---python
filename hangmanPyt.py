import random

class hangman:
	def __init__(self):
		self.randWord = self.getWord()
		self.userInterface()

	def userInterface(self):
		correctLetters = ["&"] # list of correct already apt letters
		wordLen = len(self.randWord)
		wordLen1 = len(self.randWord)
		isLetterFound = False
		win = False
		lives = 10; # number of lives

		expression = ""
		while (wordLen > 0): # display first underscore list
			wordLen = wordLen - 1
			expression = expression + "_ "
		print(expression)
		print("get letter")
		print("")
		while (lives > 0 or win): # finish when end of lives or guess right word
			isLetterFound = False
			wordLen1 = len(self.randWord)
			print("give one letter")
			letterFromUser = input()
			for x in range(0, len(self.randWord)): # is user give wrong or right letter
				if(self.randWord[x] == letterFromUser):
					# if right letter
					correctLetters.append(letterFromUser)
					wordLen1 = wordLen1 + 1
					isLetterFound = True
			if(not isLetterFound):
				#user choose wrong letter
				lives = lives - 1
			#print(correctLetters)
			win = self.showData(self.randWord, correctLetters, lives)
			if(win):
				break
		if(win):
			print("WIN !!")
		else:
			print("LOOSE !!")

	#validate letters
	def showData(self, word, letters, lives):
		# prepare list
		undercover = []
		for i in range(0, len(word)):
			undercover.append(" _")
		# display uncovered letters
		for x in range(0, len(word)):
			for i in range(0, len(letters)):
				if(word[x] == letters[i]):
					undercover[x] = word[x]
		# check is password is full undercover
		countDash = 0
		print("PASSWORD: ", undercover)
		print("REMAIN LIVES: ", lives)
		print()
		print()
		print()
		for z in range(0, len(undercover)):
			if(undercover[z] == " _"):
				countDash = countDash + 1
		if(countDash == 0):
			return True	
		return False

	# list of passwords
	def getWord(self):
		return random.choice(['japko', 'bigos', 'kisiel'])

hangman()