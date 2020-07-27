def countme(a, path):
    print(a)
    print(path)
    with open(path) as myfile:
        count = 0
        content = myfile.read()
        for chars in content:
            if a == chars:
                count += 1
    return count


# file_loc = input('What is the path for the file?')
# letter = input('What letter would you like me to count?')
print(countme('a', 'files/fruits.txt'))
