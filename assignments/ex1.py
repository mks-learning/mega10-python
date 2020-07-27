# student_grade = [9.1, 8.8, 7.5]
directory = [list, float, str, int, __builtins__, dict, tuple]
f = open('dir_of_python_classes.txt', 'w')
for i in range(0, len(directory)):
    f.write('\n \n \n Print output of ' + str(directory[i]) + ':\n')
    f.write(str(dir(directory[i])))
f.close()
