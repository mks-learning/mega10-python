# student_grade = [9.1, 8.8, 7.5]
directory = [list, float, str, int, __builtins__, dict, tuple]
f = open('dir_of_python_items.txt', 'w')
for i in range(0, len(directory)):
    f.write('\n \n \n')
    f.write('Print output of the contents of ' + str(directory[i]) + '\n')
    f.write(str(dir(i)))
f.close()
