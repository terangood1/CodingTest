win = [31, 10, 45, 1, 6, 19]

a = list(map(int,input().split()))

result = []
t = 0
win.sort()
a.sort()

for i in win:
    for j in a:
        if i == j:
            t += 1

k = a.count(0)

grade = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

result.append(grade[t])

print(result)