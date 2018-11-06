#Nesting.

try:
    age = int(input("What is your age?"))
except:
    print("Please run in a number form")
    age = int(input("What is your age?"))
gender =  input("What is your age?(male/female)")
dr = input("Have you got a Doctorite? (yes/no)")
knight = input("Have you been knighted? (yes/no)")

if dr == "yes":
    print("Dr")
else:
    if gender == "female":
        if knight == "yes":
            print("Dame")
        elif age <= 16:
            print("Miss")
        else:
            print("Ms")
    elif gender == "male":
        if knight == "yes":
            print("Sir")
        elif age <= 16:
            print("Master")
        else:
            print("Mr")
    else:
        print("Please run again, I don't understand.")