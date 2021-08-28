from sys import stdin

a = list(stdin.readline().strip())
b = list('abcdefghijklmnopqrstuvwxyz')

c = [-1 for i in range(len(b))]

for i in b:
    if i in a:
        print(a.index(i), end=" ")
    else:
        print(-1, end=" ")
