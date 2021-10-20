#입력받고 소수를 구하면 시간초과가 나와서
#미리 수소들을 구해놓고 해당범위를 출력

import math

def primenumber(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

result = []
input_data = range(2,246912)
for i in input_data:
    if primenumber(i):
        result.append(i)

while True:
    count = 0
    a = int(input())
    if a == 0:
        break
    for i in result:
        if a<i<=a*2:
            count += 1
    print(count)
