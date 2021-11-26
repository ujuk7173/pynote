# high low - class based
# The computer picks a random number
import random
def begin ():
 import random
print ("\tWelcome to 'Guess my Number'!:")
print ("\nI'm thinking of a number between 1 and 100.")
print ("Try to guess it in as few attempts as possible.\n")
 
def guess_num(num, max_guesses):
    # guessing loop
    tries = 0
    while True:
        guess = int(input("Take a guess: "))
        tries += 1
        if guess > num:
            print ("lower...")
        elif guess < num:
            print ("Higher...")
        else:
            print ("You guessed it! The number was", num)
            print ("And it only took you %d tr%s!\n" % (tries, ['ies', 'y'] [tries==1 or 0]))
            return
 
        if tries == max_guesses:
            print ("You have had %d guesses. Game over." % max_guesses)
            return
        play = input("Do you want to play again? Y/N")
        if play == "Y":
             begin ()
        if play == "N":
             print ("Well you are no fun. Bye.")
 
 
 
 
the_number = random.randrange(1,100)
max_guesses = 5
guess_num(the_number, max_guesses)