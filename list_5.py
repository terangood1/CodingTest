#https://www.acmicpc.net/step/6 5번째 

from sys import stdin

n = int(stdin.readline())

now_score = list(map(int,stdin.readline().split()))
change_score  = []

for i in now_score:
    change_score.append((i/max(now_score)*100))

print(sum(change_score)/n)
