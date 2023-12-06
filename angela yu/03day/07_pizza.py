print("welcome to python Pizza Deliveries!")
size = input("what size pizza do you want ? S , M or L :")
add_pepper = input("Do you want pepperoni ? Y or N :")
extra_cheese = input("Do you want extra cheese ? Y or N :")
bill = 0
if size == "s":
    bill = 15
    if add_pepper == "y":
        bill +=2
elif size == "m":
    bill = 20
    if add_pepper == "y":
        bill +=3
elif size == "l":
    bill =25
    if add_pepper == "y":
        bill +=3
else :
    print("please'enter the correct option")
if extra_cheese =="y":
    bill +=1
print(f"your final bill is :${bill}")

