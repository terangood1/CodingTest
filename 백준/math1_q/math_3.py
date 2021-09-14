a=int(input())
line=1
while True:
    if a<=sum(range(1,line+1)):
        break
    line+=1
line_seq = a-sum(range(1,line))

if line%2 == 0:
    m = line_seq
    s = line - line_seq + 1
else:
    m = line - line_seq + 1
    s = line_seq

print(m,'/',s,sep="")