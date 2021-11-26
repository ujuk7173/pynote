# high low basic - function based
# The computer picks a random number

import random

print ("\tWelcome to 'Guess my Number'!:")
print ("\nI'm thinking of a number between 1 and 100.")
print ("Try to guess it in as few attempts as possible.\n")
 
  
num = random.randrange(1,100)
max_guesses = 5

# guessing loop
tries = 0
while True:
    guess = int(input("Take a guess: "))
    tries += 1
    if guess > num:
        print ("Lower...")
    elif guess < num:
        print ("Higher...")
    else:
        print ("You guessed it! The number was", num)
        print ("Guessed in %d treis. \n" % (tries))
        break

    if tries == max_guesses:
        print ("You have had %d guesses. Game over." % max_guesses)
        break
   



