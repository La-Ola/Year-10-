#Triangle

Yes = int(input("do you want to make a Triangle? 1Yes or 2No."))

while Yes == 1:
    h = int(input("Enter a height from 2-10"))
    w = int(input("Enter a width to be the same as the height"))
    w = 1
    for i in range (h):
        print (w * "*")
        w = w + 1
    Yes = int(input("do you want to make a quadrilateral? 1Yes or 2No."))
