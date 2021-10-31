#브루트포스 알고리즘
n = int(input())

a = 666
count = 0
while(True):
    if "666" in str(a):
        count += 1
        if count == n:
            print(a)
            break

    a += 1