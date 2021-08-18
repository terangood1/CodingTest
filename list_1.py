#https://www.acmicpc.net/step/6 1번문제

from sys import stdin

a = int(stdin.readline())

b = list(map(int, stdin.readline().split()))

b.sort() #정렬

print(b[0], b[-1]) #0번쨰 인덱스 최솟값 -1번째 인덱스 최댓값
