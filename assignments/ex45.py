with open('~/Desktop/bear.txt', 'r') as myfile:
    content = myfile.read()
    content = content[0:91]
print(content)
