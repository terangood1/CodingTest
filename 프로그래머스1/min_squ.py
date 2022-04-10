s = [[60, 50], [30, 70], [60, 30], [80, 40]]
answer = []
answer2 = []
for x in s:
    answer.append(max(x))
    
for x in s:
    answer2.append(min(x))
    
print(answer)
print(answer2)
        
print(max(answer))