#https://www.acmicpc.net/step/6 6번째 

from sys import stdin

n = int(stdin.readline())
result = []

sum = 0
for i in range(n):
    result.append(stdin.readline().strip())
score = 0
last_score = 0
for k in result:
    if k == 'o':
        score +=1
        last_score += score
    else:
        score = 0
print(score)
