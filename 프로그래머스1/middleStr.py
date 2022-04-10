s = input()
#짝수
# k = len(s)
# print(s[int(len(s)/2)-1],s[int(len(s)/2)])

# t = 'abcde'

# q = len(t)

# print(t[int((q+1)/2)-1])

# z = 'a' + 'b'
# print(z)
answer = ''
k = len(s)
if k%2 == 0:
    answer = s[int(len(s)/2)-1] + s[int(len(s)/2)]
else:
    answer = s[int((len(s))+1/2)-1]

print(answer)