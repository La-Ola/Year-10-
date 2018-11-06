#list2
#Part1
##students = ["Chloe","Beth","Alex","David","Emma","Bruce","Chris","Sam"]
##x = len(students)
##print (x)
##for i in range(x):
##    print (students[i])

#Part3
students = ["Chloe","Beth","Alex","David","Emma","Bruce","Chris","Sam"]
x = len(students)
name = input("What name are you looking for?")
##print (x)
if name in students:
    for i in range(x):
        if name == students[i]:
            print (students[i],"Found in list at position", i+1)
else:
    print ("Name not recognised")

#Part4
##students = ["Chloe","Beth","Alex","David","Emma","Bruce","Chris","Sam"]
##girlsnames = ["Chloe","Beth","Emma"]
##x = len(students)
##name = input("What name are you looking for; Chloe, Beth, Alex, David, Emma, Bruce, Chris, Sam?")
##print (x)
##if name in girlsnames:
##    for i in range(x):
##        if name == students[i]:
##            print (students[i],"is a Girl and is found in position ", i+1)
##else:
##    for i in range(x):
##        if name == students[i]:
##            print (students[i],"is a Boy and is found in position ", i+1)

#Part5
##TGS =[]
##TKS = []
##FYS = []
##PNS = []
##P = []
##for i in range (10):
##    name = input("Please enter your name.")
##    house = input("Please enter your house; TG,TK, FY, PN. If you are not in a house input P.")
##    if house == "TG":
##        TGS.append(name)
##    elif house == "TK":
##        TKS.append(name)
##    elif house == "FY":
##        FYS.append(name)
##    elif house == "PN":
##        PNS.append(name)
##    elif house == "P":
##        P.append(name)
##print("In Tregantle we have",TGS)
##print("In Tregonhawke we have",TKS)
##print("In Frethy we have",FYS)
##print("In Polawn we have",PNS)
##print("In Miscellanious we have",P)
##
###Part6
##
##mystring = "Chloe, Beth, Alex, David, Emma, Bruce, Chris, Sam"
##print (mystring.split( ))
##mystring2 = "Chloe Beth Alex David Emma Bruce Chris Sam"
##print (mystring2.split( ))
##




