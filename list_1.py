from sys import stdin

a = int(stdin.readline())

b = list(map(int, stdin.readline().split()))

b.sort()

print(b[0], b[-1])