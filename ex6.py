my_name  = input("Please input your name\n> ")
my_age = input("Please input your age\n> ")
my_height = input("Please input your height in cm\n> ")
my_weight = input("Please input your weight in kg\n> ")
my_eyes = input("Please input your eye color\n> ")
my_hair = input("Please input your hair color\n> ")

if int(my_age) < 18:
    print("You are under 18 years old")
elif int(my_age) > 60:
    print("You are over 60 years old")
else:
    print("You are between 18 and 60 years old")

if int(my_height) < 140:
    print("You are under 140cm in height")
elif int(my_height) > 180:
    print("You are over 180cm in height")
else:
    print("You are between 140cm and 180cm in height")

if int(my_weight) < 60:
    print("You are under 60kg in weight")
elif int(my_weight) > 120:
    print("You are over 120kg in weight")
else:
    print("You are between 18kg and 60kg in weight")

input()
