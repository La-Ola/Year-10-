
#MULTIPLIER

play = str(input("Would you like a multiplier program? (Please type 'Yes'.)"))

while play== "Yes":
    sn = int(input("What number would you like you start point to be?"))
    en = int(input("How many times would you like it to repeat?"))
    m = int(input("What would you like your multiplier to be?"))

    print ("**********",m,"TIMES TABLE **********")
    for i in range (sn,en):
        ans = i * m
        print ("",i,"*",m,"=",ans)

    play = str(input("Would you like to reuse the program? Please enter Yes or No."))
print("Goodbye.")