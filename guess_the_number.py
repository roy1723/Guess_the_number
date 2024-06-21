#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random
print(art.logo)
number_list = []
for i in range(1, 101):
  number_list.append(i)
def guess_number():
  return random.choice(number_list)
def compare(guess, answer):
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it! The answer was {answer}.")
    exit()
print("Welcome to the Number guessing game!")
print("I am thinking of a number between 1 and 100. ")
answer = guess_number()
print(f"psst, the correct answer is {answer}")
difficulty = input("choose a diffculty level. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
else:
  attempts = 5
while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number. ")
  guess = int(input("Make a guess: "))
  compare(guess, answer)
  attempts -= 1
  
  