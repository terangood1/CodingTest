import math
a,b,v = map(int,input().split())

result = 1
count = 0
if a>=v:
    print(result)
else:
    length = v-a
    time = a-b
    print(result + math.ceil(length/time))