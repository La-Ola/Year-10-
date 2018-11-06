#Calculator
first_num = int(input("Please enter FIRST NUMBER"))
second_num = int(input("Please enter SECOND NUMBER"))

print("enter 1 for a '+'")
print("enter 2 for a '-'")
print("enter 3 for a '/'")
print("enter 4 for a '*'")

choice = int(input())

if choice==1:
    operator = "+"
    answer = first_num + second_num

elif choice==2:
    operator = "-"
    answer = first_num - second_num

elif choice==3:
    operator = "*"
    answer = first_num * second_num

elif choice==4:
    operator = "/"
    answer = first_num / second_num

print (first_num,operator,second_num,"=",answer)