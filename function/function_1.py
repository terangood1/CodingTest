# https://www.acmicpc.net/step/5 1번

k = [1,2,3,4]
def solve(a):
    result = 0
    for i in a:
        result += i
    return result

print(solve(k))