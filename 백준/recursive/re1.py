#0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*recursive(n-1)

a = int(input())

print(recursive(a))

