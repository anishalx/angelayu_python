print("Welcome to Treasure island .")
print("Your mission is to find the treasure .")
side = input("Which side you want to go ? Left or Right :\n").lower()

if side == "left":
    action =input("What you want to do next ? Swim or Wait :").lower()
    if action=="wait":
        door=input("Which door you want to choose ? Red ,Blue or Yellow :").lower()
        if door =="yellow":
            print("Hurray! You won the game .you got the treasure .")
        else :
            print("Opps! Better luck for next time .GAMEOVER")
    else:
        print("Opps! you choosed a wrong action . GAMEOVER ")
    
else :
    print("Opps! you choosed a wrong side GAMEOVER")
