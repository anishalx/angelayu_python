'''year = int(input("Enter your year here :"))
if (year % 4 ==0 or year %100 ==0) and year % 400 !=0 :
    print(f"Your year is {year} is a leap year .")
else :
    print("Opps! your year is not a leap year ")
'''


years = int(input("Enter your year here :"))
if years % 4==0:
    if years % 100==0:
        if years %400==0:
            print(f"Your year is {years} is a leap year .")
        else:
            print("Opps! your year is not a leap year ")
    else:
        print(f"Your year is {years} is a leap year .")
else:
    print("Opps! your year is not a leap year ")

            