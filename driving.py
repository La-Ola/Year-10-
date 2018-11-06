print ("               Welcome to DVLA driving test.")
print ("**************************************************************")

years = int(input("How many years have you been driving for?"))
points = int(input("How many penalty point do you have?"))

if years <=2 and points >=6:
    print("-------------LICENCE SUMMARY-------------")
    print("   YOUR LICENCE HAS BEEN DISQUALIFIED.")
    print("-----------------------------------------")

elif years >=2 and points >=12:
     print("-------------LICENCE SUMMARY-------------")
     print("    YOUR LICENCE HAS BEEN TIME-BANNED.")
     print("-----------------------------------------")

else:
     print("-------------LICENCE SUMMARY-------------")
     print("     YOUR LICENCE IS OKAY, CONTINUE.")
     print("-----------------------------------------")
