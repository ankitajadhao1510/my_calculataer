student_scores = input("Input a list of student scores ").split()
for highest in range(0, len(student_scores)):
  student_scores[highest] = int(student_scores[highest])
print(student_scores)
highest_score = 0
for highest in student_scores:
  if highest > highest_score:
    highest_score = highest

print(f"The highest score in class is : {highest_score}")
