print("I am thinking of a number between 1 and 100. Guess a number, and I will tell you know if you're too high, too low, or got it right!")
print("Goodluck!\n")

import random
computer_number = random.randint(1, 100)                #range is from 1-100


guess = int(input("Give me a number: "))                #storing user's input in a variable called guess
counter = 1                                             #set counter eqaul to 1

while guess != computer_number:                         #this while loop will stop running once the value of
    if guess > computer_number:                         #guess equals the value of computer number
        print("Too High!")
        counter += 1                                    #incrementing the value of counter by 1
        guess = int(input("Give me a number: "))
    elif guess < computer_number:
        print("Too Low!")
        counter += 1
        guess = int(input("Give me a number: "))
    else:
        print("I don't know")

print("\nCongratulations! You guessed it right in {} tries.".format(counter))

