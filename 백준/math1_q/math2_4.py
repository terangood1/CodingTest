from sys import stdin
import math

a,b = map(int, stdin.readline().split())
def primenumber(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

for j in range(a,b+1):
    if(primenumber(j)):
        print(j)
