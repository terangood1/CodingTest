#https://www.acmicpc.net/step/6 4번째 

from sys import stdin

data = []

for i in range(10):
    data.append((int(stdin.readline()))%42)

data = set(data)

print(len(data))


