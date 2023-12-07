print("Welcome to love calculator!")
name1 = input("what is your name ?\n")
name2 = input("what is your lover name ?\n")
name = name1 + name2
lower_name = name.lower()

t = lower_name.count("t") 
r = lower_name.count("r") 
u = lower_name.count("u") 
e = lower_name.count("e") 
true = t + r + u + e
l = lower_name.count("l") 
o = lower_name.count("o") 
v = lower_name.count("v") 
e = lower_name.count("e") 
love = l + o + v + e
score =int(str(true)+str(love))

if (score<10) or (score>90):
    print(f"your score is {score},you go togrther like coke and mentos")
elif score>=40 and score<=50:
    print(f"your score is {score},you are alright together")
else:
    print(f"your love score is {score}") 