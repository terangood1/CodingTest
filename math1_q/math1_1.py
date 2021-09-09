a,b,c = list(map(int, input().split()))
n = 1
if b>=c:
    print('-1')
else:
    k = int(a/(c-b))
    n += k
    print(n)

