a = [1,2,3,4,5,6,7,8]

c = []
for i in a:
    if a[-1:] == [i]: continue
    c.append(i)

print(c)