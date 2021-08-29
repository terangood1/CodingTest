
a = input().lower()
b = list(set(a)) 
result = []

for i in b:
    word = a.count(i) 
    result.append(word)  
if result.count(max(result)) >= 2:
    print('?')
else:
    k = result.index(max(result))
    print(b[k].upper())
