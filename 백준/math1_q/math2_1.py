n = int(input())

k = list(map(int,input().split()))
result = 0

for i in k:
    if i != 1:
        if i == 2:
            result += 1
        else:
            for j in range(2,i):
                if i%j == 0:
                    break
                elif j == i-1:
                    result += 1
                
print(result)