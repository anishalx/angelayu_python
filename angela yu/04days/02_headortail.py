import random
print("Hello ,Toss your coin virtually here ")
choosenside = input("choose HEAD or TAIL \n").lower()
head =0
tail = 1
random_num = random.randint(0,1)
if random_num ==head:
    print("Hurray !You won the toss ")
else:
    print("Opps! You lost the toss")
# print(random_num)



