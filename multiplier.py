
#MULTIPLIER

play = str(input("Would you like a multiplier program? (Please type 'Yes'.)")) #makes sure that the user input is a string

while play == "Yes":
    StartNumber = int(input("What number would you like you start point to be?"))
    EndNumber = int(input("How many times would you like it to repeat?"))
    multiplier = int(input("What would you like your multiplier to be?"))

    print ("**********",multiplier,"TIMES TABLE **********")
    for index in range (StartNumber, EndNumber):
        ans = index * multiplier
        print (index,"*",multiplier,"=",ans)

    play = str(input("Would you like to reuse the program? Please enter Yes or No.")) #continues or exits the loop
print("Goodbye.")
