#https://www.acmicpc.net/step/6 2번째 
from sys import stdin

result = []
for i in range(9):
    result.append(int(stdin.readline()))

print(max(result))  # 리스트 최댓값
print(result.index(max(result))+1) #최댓값 인덱스 +1