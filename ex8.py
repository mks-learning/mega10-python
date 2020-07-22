student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
x = []
for i in range(0,len(student_grades)):
    if student_grades[i] == 10.0:
        x.append(student_grades[i])
print(len(x))
