#CUBE

Yes = int(input("do you want to make a quadrilateral? 1Yes or 2No."))

while Yes == 1:
    width = int(input("Enter a width from 2-10"))
    height = int(input("Enter a width from 2-10"))
    for i in range (height):
        print (width * "*")
    Yes = int(input("do you want to make a quadrilateral? 1Yes or 2No."))
