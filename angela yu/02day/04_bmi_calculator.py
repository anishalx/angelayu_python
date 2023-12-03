height = input("Enter your height here in m : ")
weight = input("Enter your weight here in kg :")
# print(type(height))
# print(type(weight))
new_height = float(height)
new_weight = int(weight)
bmi = new_weight/new_height**2
print(int(bmi))
