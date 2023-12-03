print("welcome to the roller coaster ride !")
height = int(input("Enter your height here in cm  : "))
if height > 120 :
    print("Hurray! you can ride ")
    age = int(input("Now enter your age here : "))
    if age <12:
        print("you have to pay $5")
    elif age <=18: 
        print("you have to pay $7")
    else:
        print("you have to pay $12")
else :
    print("opps! you can't ride")