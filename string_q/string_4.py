from sys import stdin

a = int(stdin.readline())

for i in range(a):
    b,c = stdin.readline().split()
    b = int(b)
    for i in c:
        print(i*b, end='')
    print()

        

