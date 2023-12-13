student_heights = input("Enter a list of students heights\n").split()
# print(student_heights)
# print(type(student_heights))
# Convert the string list to an integer list.
int_list = [int(i) for i in student_heights]
# print(int_list)
highest_score = 0
for max in int_list :
    if highest_score < max:
        highest_score=max
print(f"The heighest score is {highest_score}")
# print(type(max))

