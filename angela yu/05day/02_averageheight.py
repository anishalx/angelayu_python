student_heights = input("Enter a list of students heights\n").split()
# for n in range(0, len(student_heights)):
#     student_height[n] = int(student-heights[n])
# print(student_heights)
# student_height = int(student_heights)

total_heights = 0
for height in student_heights:
    # print(type(height))
    heights = int(height)
    total_heights += heights
# print(total_heights)

number_of_student =0
for student in student_heights:
    # student=(len(student_heights))
    students = int(student)
    number_of_student += 1
    # number_of_student += student
# print(student)
# print(type(student))

average_height = total_heights/number_of_student
print(average_height)
# print(type(average_height))