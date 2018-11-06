#Colour mixer

c = int(input("Would you like to mix colours? (1)YES (2)NO"))

while c == 1:
    c1 = int(input("Choose you first colour to mix. (1)RED (2)BLUE (3)BLACK"))
    c2 = int(input("Choose you first colour to mix. (1)RED (2)BLUE (3)BLACK"))

    if c1 == 1 and c2 == 1:
        print ("RED")
    elif c1 == 1 and c2 == 2:
        print ("MAGENTA")
    elif c1 == 1 and c2 == 3:
        print ("CRIMSON")
    elif c1 == 2 and c2 == 1:
        print ("MAGENTA")
    elif c1 == 2 and c2 == 2:
        print ("BLUE")
    elif c1 == 2 and c2 == 3:
        print ("NAVY")
    elif c1 == 3 and c2 == 1:
        print ("CRIMSON")
    elif c1 == 3 and c2 == 2:
        print ("NAVY")
    elif c1 == 3 and c2 == 3:
        print ("BLACK")
    c = int(input("Would you like to CONTINUE TO mix colours? (1)YES (2)NO"))