import random
import os, sys
from time import sleep
import cursor


def load_words():
    lines =open('words.txt', 'r').readlines()
    line = lines[0]
    words =line.split()
    myword = random.choice(words)

    return myword


#wordlist = load_words()
#print(wordlist)


os.system('cls')

word = load_words()
#word1 = 'america'

cursor.hide()
print('''			    Welcome to''')
wcText = '''		Wheel Of Fortune - Python Mini Project by


					




		@@@  @@@     @@@      @@@@@@      @@@  @@@      @@@@@@      @@@@@@@      @@@@@@@@
		@@@  @@@     @@@     @@@@@@@      @@@  @@@     @@@@@@@@     @@@@@@@@     @@@@@@@@
		@@!  !@@     @@!     !@@          @@!  @@@     @@!  @@@     @@!  @@@     @@!
		!@!  @!!     !@!     !@!          !@!  @!@     !@!  @!@     !@!  @!@     !@!
		@!@@!@!      !!@     !!@@!!       @!@!@!@!     @!@  !@!     @!@!!@!      @!!!:!
		!!@!!!       !!!      !!@!!!      !!!@!!!!     !@!  !!!     !!@!@!       !!!!!:
		!!: :!!      !!:          !:!     !!:  !!!     !!:  !!!     !!: :!!      !!:
		:!:  !:!     :!:         !:!      :!:  !:!     :!:  !:!     :!:  !:!     :!:
 		::  :::      ::     :::: ::      ::   :::     ::::: ::     ::   :::      :: ::::
 		:   :::     :       :: : :        :   : :      : :  :       :   : :     : :: ::'''

for ch in wcText:
	sys.stdout.write(ch)
	sys.stdout.flush()
sleep(4)



os.system('cls')

cursor.show()


def Guess(Choice):
	if Choice == 'y':
		ChoosingWord()
		
	elif Choice == 'n':
		choosingLetter()
		os.system('cls')
	else:
		print("Unsupported input")
		print("Exiting...")
		sleep(2)
		exit()
	os.system('cls')




def ChoosingWord():
	playin = input("Enter word \n>").upper()
	if playin == word:
		#print("The Word is ",playin)
		print(playin," is the correct answer")
		exittext = input('Want to exit (y/n)? \n>')
		ExitOrTryAgain(exittext)
		os.system('cls')

	else:
		#print(new_state)
		print(playin,"is the wrong answer :(")
		print("Do you Want to Try again ")
		print("Enter 'y' to continue or 'a' to Reveal the Answer and Exit ")
		et = input("Your Choice is? \n>")
		if et == 'a':
			print("The correct answer is ", word)
			print("Exiting...")
			sleep(4)
			exit()

		elif et == 'y':
			pass
		else:
			exit()
		os.system('cls')



	
def choosingLetter():
	global new_state
	chosen_word = word.upper()
	state = "_"*len(chosen_word)
	guess = input("Guess the letter: \n>").upper()
	new_state = [(chosen if chosen == guess else blank) 
				for chosen, blank in zip(chosen_word, state) ]
	' '.join(new_state)
	print(new_state)
	sleep(3)
	return new_state
	os.system('cls')




def ExitOrTryAgain(option):
	if option == 'y':
		exit()
	elif option == 'n':
		pass
	else:
		print("Unsupported input")
		exit()
		print("Exiting...")
		sleep(2)
	os.system('cls')


while True:
	blank = len(word)* '_ '
	print("Guess the word :) ",blank)
	print("Enter 'y' to guess the word")
	print("Enter 'n' to guess the letter")
	Choice = input("Enter your Choice (y/n): \n>")

	os.system('cls')
	Guess(Choice)


	sleep(1)
	os.system('cls')