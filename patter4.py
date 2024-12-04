num=5
for line in range (1,num+1):
    for sp in range(num-line):
        print(' ',end=' ')
    for st in range(line):
        print('*',end=' ')
    print()
