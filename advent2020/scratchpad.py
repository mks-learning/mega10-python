import numpy as np

f = open('D3-input.txt', 'r')
curse = [line for line in f.readlines()]
f.close()
i = 0
while i < len(curse):
    print()