#This program works slight different from one on Canvas but the ending result is same
#Let's suppose your imaginary number is 42 and the Random Generator guessed the number 32
#You tell me go to higher because your number is bigger which is 42 in this case
#Let's say for the second time, the Random Generator guessed the number 89
#You tell me go come lower because your number is 42
#I think you get the point.

print("Please think of a number between 1 and 100. I'll try to guess your number. Tell me to go high, low, or if I'm correct.")

import random
lowest_value = 0                                            #set variable lowest_value equals 0
highest_value = 100                                         #set variable highest_value equals 100
my_response = ""                                            #setting equal to empty string so I can access the value of it in my while loop
random_num = random.randint(lowest_value, highest_value)    #range 0-100
counter = 1                                                 #set counter equals 1


while my_response != "c":                                   #this while loop will stop running once my_response eqauls "c"
    print("\nMy guess is: {}".format(random_num))
    my_response = input("go (h)igh, go (l)ow, or (c)orrect?")   #storing the value of user's input in my_response
    if my_response == "h":
        lowest_value = random_num + 1
        random_num = random.randint(lowest_value, highest_value)
        counter += 1                                        #increment the counter by 1
    elif my_response == "l":
        highest_value = random_num - 1
        random_num = random.randint(lowest_value, highest_value)
        counter += 1
    elif my_response == "c":
        print("\nWoo-Hoo!, I guessed your number in {} tries!".format(counter))
        break                                                                       #break statement breaks out of the loop
    else:
        print("Try it again! I don't know what you are typing!")


