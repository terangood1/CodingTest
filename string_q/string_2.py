from sys import stdin

a = int(stdin.readline())
b = list(map(int, stdin.readline().strip()))

print(sum(b))