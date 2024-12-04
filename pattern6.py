num=5
spaces=0
for line in range (num*2-1,0,-2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(line):
        print('*',end=' ')
    print()
    spaces +=1
