#https://www.acmicpc.net/step/6 3번째 
from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())

multiple = list(str(a*b*c)) #str변경  

for i in range(10):
    print(multiple.count(str(i)))
