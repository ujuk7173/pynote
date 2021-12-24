import random
import time
print('Press enter to start!')
input()
# log the starting time
start = time.time() 
# create a list of words
words = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf", "veggie pizza is the best pizza"]

# score
count = 0 
# repeat 5 times
for i in range(5):
	dunno = random.choice(words)
	print(dunno)
	# get user input
	answer = input('Enter: ')
	if dunno == answer:
		print('correct!')
		count = count + 1
	else:
		print('incorrect!')
# end
end = time.time()
your_time = end - start
print(format(your_time,".2f"))
print('score:',count,'yay')