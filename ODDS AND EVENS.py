#Odds and Evens

print ("*****ODDS AND EVENS BETWEEN YOUR CHOSEN NUMBER AND 50*****")
num = int(input("Choose a number between 1 and 50."))

print("****THE EVENS****")
x = num
while x < 50:
    if x%2 == 0:
        print (x)

    x = x + 1

print("****AND NOW THE ODDS****")
x = num
while x < 50:
    if x%2 == 1:
        print (x)

    x = x + 1
