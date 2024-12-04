num=3
spaces=num-1
for line in range(1,num*2,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(line):
        print('*',end=' ')
    print()
    spaces -=1
