a,b = list(map(list ,input().split()))

a.reverse()
b.reverse()
ar = "".join(a)
br = "".join(b)

if int(ar)>int(br):
    print(ar)
else:
    print(br)