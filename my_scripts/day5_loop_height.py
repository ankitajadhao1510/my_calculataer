student_height = input('Input a list of student height- ').split()
for height in range(0, len(student_height)):
    student_height[height] = int(student_height[height])
print(student_height)

total_height = 0
for height in student_height:
    total_height += height
print(f"total height- {total_height}")

number_of_student = 0
for student in student_height:
    number_of_student += 1
print(f"no of student- {number_of_student}")

avg_height = round(total_height/number_of_student)
print(avg_height)