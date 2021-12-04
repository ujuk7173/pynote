import random
import time

words = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf", "veggie pizza is the best pizza"]

print("Press 'enter' to start!")
input()
start = time.time()

question = random.choice(words)
n = 1
while n <= 5:
    print("-- word #{} --".format(n))
    print(question)
    answer = input()

    if question == answer:
        print("** Success! **")
        n = n+1
        question = random.choice(words)

    else :
        print("** Fail! **")

end = time.time()
time_game = end - start
time_game = format(time_game, ".2f")
print("time :", time_game, "seconds")