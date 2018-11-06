
#welcoming screen
print(" WELCOME TO SUBWAY, PLEASE PLACE YOUR ORDER")
print("********************************************")

#order screen
print("Please enter the number in brackets before the option to select.")
fill = int(input("Fillings; (1)Cheese & Tomato (2)Italian Bacon & Peperoni (3)Tuna &Mayo (4)Turkey & Ham (5)Chicken Teriyaki (6)Steak & Cheese"))
size = int(input("Size; (1)6inch Sub (2)12inch Sub"))
bread = int(input("Bread type; (1)Plain (2)Wheat (3)Italian (4)Cheese & Herb"))
eat = int(input("If you would like to eat in, please press (1) If you would like to take away, please press (2). If you eat i it will be a 5% increase on your pay. "))

#cost variables
if fill == 1:
    fillc = 0.95
elif fill == 2:
    fillc = 1.10
elif fill == 3:
    fillc = 0.95
elif fill == 4:
    fillc = 1.35
elif fill == 5:
    fillc = 1.40
elif fill == 6:
    fillc = 1.95

if size == 1:
    sizec = 1.65
elif size == 2:
    sizec = 2.05

if bread == 1:
    breadc = 0.40
elif bread == 2:
    breadc = 0.65
elif bread == 3:
    breadc = 0.75
elif bread == 4:
    breadc = 0.80

if eat == 1:
    cost = fillc + sizec + breadc / 100 * 5
    incost = cost + fillc + sizec + breadc
    print("Your payment is £", (round(incost,2)) ,". Thankyou for using Subway.")
elif eat == 2:
    outcost = fillc + sizec + breadc
    print("Your payment is £", (round(outcost,2)) ,". Thankyou, for using Subway")