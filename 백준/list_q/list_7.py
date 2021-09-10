from sys import stdin

test_case = int(stdin.readline())
result = []


for i in range(test_case): # i는 0~ 케이스 수
    a= list(map(int, stdin.readline().split()))
    avg = sum(a[1:])/a[0] # 첫번째 케이스 평균
    count = 0
    score = a[1:]
    for k in score:
        if avg<k:
            count +=1
    result.append((count/a[0])*100)

for i in result:
    print("{:.3f}%".format(i))



    
