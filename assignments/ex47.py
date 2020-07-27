with open('files/bear.txt', 'r') as myfile:
    content = myfile.read()
    output = content[0:91]
    mywork = open('files/first.txt', 'w')
    mywork.write(output)
    mywork.close()
