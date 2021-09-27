

#테스트 케이스 입력
t = int(input())

#결과 저장
result = []

#층 수, 방의 수 , 몇번째 손님
for _ in range(t):
    f,rn,c = map(int,input().split())
    a = c%f
    b = c//f+1
    if a== 0:
        a = f
        b -= 1
    result.append(a * 100+b)
#결과 출력
for i in result:
    print(i)
