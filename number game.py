
#Guessing Gameimport random
import random
number= random.randint (1,50)
ans = int(input("Choose a number between 1 - 50."))
while ans != number:
    if ans<number:
        print ("you are too low")
    elif ans>number:
        print ("you are too high")
    ans = int(input("guess again"))
print("well done!")