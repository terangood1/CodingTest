#https://www.acmicpc.net/step/6 6번째 

from sys import stdin

n = int(stdin.readline())
result = []

for i in range(n):
    result.append(stdin.readline().strip())

score_list = []
for k in result:
    score = 0
    last_score = 0
    for j in k:
        if j == 'O':
            score +=1
            last_score += score
        else:
            score = 0
    score_list.append(last_score)


for i in score_list:
    print(i)
