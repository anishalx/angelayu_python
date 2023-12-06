print("welcome to the roller coaster ride !")
height = int(input("Enter your height here in cm  : "))
if height > 120 :
    print("Hurray! you can ride ")
    age = int(input("Now enter your age here : "))
    bill=0
    if age <12:
        bill=5
        print("Child,you have to pay $5")
    elif age <=18: 
        bill=7
        print("Youth,you have to pay $7")
    else:
        bill=12
        print("Adult,you have to pay $12")
    photo = input("You want photo or not ? Y or N :")
    if photo == "y":
        bill += 3
        print(f"your final bill is :${bill}")
    else:
        print("Enjoy your ride" )
else :
    print("opps! you can't ride")