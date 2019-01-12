#Quiz
score = 0
print ("Score",score,"/5") #score not in brackets refers to the variable

ans= input("Question 1) How many lives do cats have?") #inputs users answer to the variable
if ans=="9": # if answer is equal to 9 do this 
    print("Correct!")
    score = score + 1 #adds one to the score
    print ("Score",score,"/5")

else: #if not do this
    print("Incorrect")
    print("Score", score,"/5")

ans = input("Question 2) What colour is the sky?")
if ans=="blue":
    print("Correct!")
    score = score + 1
    print ("Score",score,"/5")

else:
    print("Incorrect")
    print("Score", score,"/5")

ans= input("Question 3) When did World War Two end (year)?")
if ans=="1945":
    print("Correct!")
    score = score + 1
    print ("Score",score,"/5")

else:
    print("Incorrect")
    print("Score", score,"/5")

ans= input("Question 4) Who wrote Moby Dick?")
if ans=="herman melville":
    print("Correct!")
    score = score + 1
    print ("Score",score,"/5")

else:
    print("Incorrect")
    print("Score", score,"/5")

ans= input("Question 5) Where was doctor foster when he stood in a very deep puddle?")
if ans=="Gloster":
    print("Correct!")
    score = score + 1
    print ("Score",score,"/5")

else:
    print("Incorrect")
    print("Score", score,"/5")

print("This is your final score", score) #prints final score
