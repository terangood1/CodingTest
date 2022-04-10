s = 'aaaa a'
k = []
k.append(s.split())
answer = []
for i in k:
    #print(i)
    for j in i:
        #print(j)
        for z in range(len(j)):
            if z%2 == 0:
                j = list(j)
                #print(j[z])
                j[z] = j[z].upper()
        answer.append(j)
answer2 = []
for i in answer:
    answer2.append(''.join(i))

print(' '.join(answer2))
        
        

