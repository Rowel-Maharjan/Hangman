import os #to clear screen
import random #to get random character

print("\n")
a = "Welcome to Hangman Game"
print(a.center(50,"*"),"\n")

print("""Rules of the game
a) You got 8 chances to find the word
b) Each time you choose the incorrect letter your chance decreases by 1 and you lose when your chances decreases to zero
c) If you choose the correct word your chance won't decrease and will win when you find all the letters of the word.
d) If the length of word is greater than 6, some letter will be given as hint. \n\n""")

chance = 8  
guessed_letter = []
while(True):  #To input only from a-z or A-z
  word = input("Player1: Enter the word: ").lower()
  if(word.isalpha() == False):  # it is true when string is a-z or A-Z otherwise it is false
    print("Special character is not allowed. Enter word again.")
    continue
  else:
    length = len(word)
    break
count = 1   # it is declared to run random.choice function only once in while loop
os.system("cls")

while(chance>0):
  if count == 1:
    if length >= 7:
      character = random.choice(word)   # choose random character from input word
      guessed_letter.append(character)   #character need to be append in guessed_letter
    count = count-1

  display_word = " "
  for letter in word:  #This for loop is to display word as a string
    if letter in guessed_letter:
      display_word = display_word + letter + " "
    else:
      display_word = display_word + "_ "
  print(display_word)

  if "_" not in display_word:
    Win = "Congratulations!!! YOU WON THE GAME"
    print("\n",Win.center(50))
    break;
  
  print("Guessed-letters =",guessed_letter)
  print("Chance left =",chance)
  guess = input("\nPlayer2: Guess the letter: ").lower()

  length_of_guess = len(guess)
  if guess in guessed_letter:
    os.system("cls")
    print("You have already guessed "+guess+". Guess another letter")
    continue

  guessed_letter.append(guess)

  if guess in word:
    os.system("cls")
    print("You guessed it correctly")  

  if length_of_guess > 1:
    os.system("cls")
    print("You can guess only one at a time. Guess single letter at a time")
    continue

  if guess not in word:
    os.system("cls")
    chance = chance - 1
    if chance >= 1:
      print("You are incorrect. Try another guess.")

else:
  os.system("cls")
  print(display_word)
  print("You are incorrect")
  print("Chance left = 0")
  Lose = "YOU LOSE THE GAME"
  print("\n",Lose.center(50))

  print("THE WORD WAS",word)
