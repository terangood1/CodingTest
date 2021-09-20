# 3층의 2호에 살려면 자신의 아래 2층의 1호부터 2호까지 사람들의 수의 합만큼 사람들을데려와 살아야한다

# k층에 n호에는 몇명이 살고 있는지 출력 1호에는 1명이 산다
# 0층부터 있고 각층에는 1호부터 있음 0층의 1호에는 1명 2호에는 2명 첫줄에는 k 둘째줄에는 n 2층 1호 // 
# 2층에 1호에는 몇명이 사냐
# 1층에 1호 한명 


#몇 몇호에 사는 함수 하나 만들고 결과를 더한다
def home(a,b):
    
    return a+b


#테스트 케이스 입력
t = int(input())

#결과 저장
result = []

#입력값 
for i in range(t):
    a = int(input())
    b = int(input())
    result.append(home(a,b))

#결과 출력
for i in result:
    print(i)

