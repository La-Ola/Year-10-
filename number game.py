
#Guessing Gameimport random
import random #imports the random dictionary
number= random.randint (1,50) #chooses a random integer between given number and asigns it to the variable
ans = int(input("Choose a number between 1 - 50.")) #turns the string input into an integer
while ans != number: #wont break loop until answer is the same as the number chosen at random
    if ans<number: #answer is less than number 
        print ("you are too low")
    elif ans>number: #answer is more than number 
        print ("you are too high")
    ans = int(input("guess again"))
print("well done!")
