n = int(input())
result = []
for i in range(n):
    a,b = map(int,input().split())
    result.append((a,b))

for i in result:
    rank = 1
    for j in result:
        print('t',i, j)
        if i[0]<j[0] and i[1]<j[1]:
            rank += 1
    print(rank,end=" ")