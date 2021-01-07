with open('D4-input.txt', encoding = 'utf-8') as stuff:
    #this line takes the file and make each line a list item within a larger list
    x = [l.strip(' ') for l in stuff]
    print(x)
    # flatList = [item for elem in x for item in elem]
    # print(flatList)
