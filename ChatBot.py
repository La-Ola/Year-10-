#CHATBOT

import random
botname = ["Boo","Phil","Brandon","Jade","Freddy","Bill","Ben","FlowerPotMan"]
num = random.randint(0,8)

import datetime
hour = datetime.datetime.now().hour
if hour > 12:
    t = "Good Afternoon"
    print (t)
elif hour < 12:
    t = "Good Morning"
    print (t)
print ("What is your name?")
user_name = input()
print ("Oh hi ",user_name,", my name is ", botname[num])

print ("How are you?")
response = input()
responce_list = ["good","alright","cool","not bad","well","fine"]
if response in responce_list:
    print ("Cool! Same to be honest.")
else:
    print ("Naww, whats up??")
    why = input()
    print ("It's okay, you will be fine, stay strong. ", user_name)

print ("What is your favourite colour???")
colour = ["red","green","blue","purple","orange","black","white"]
ans = input()

while ans not in colour:
    print ("I don't understand! Please say your next favourite?")
    ans = input()

print ("Same!!!!")
print ("So, how old are you?")
age = int(input())
print ("Are you a girl or boy???")
gender = input()

if age >= 21:
    if gender == "girl":
        print ("Should'nt you be cleaning like a good housewife")
    elif gender == "boy":
        print ("Add me on Ps4 mate")
elif age <= 21:
    if gender == "girl":
        print ("Don't talk to strangers... go to school, little girl")
    elif gender == "boy":
        print ("Get to school, don't talk to strangers. Are you dumb?")
