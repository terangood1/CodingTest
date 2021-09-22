
import re

a = input()
#1
a = a.lower()
#2
case1 = "~!@#$%^&*()=+[{]}:?,<>/"
for i in case1:
    if i in a:
        a = a.replace(i,"")
#3 
a = re.sub("\.+",".",a)
#4
if a[0] == '.':
    if len(a)>=2:
        a = a[1:]
    else:
        a = "."
#5
if a[-1] == '.':
    a = a[:-1]

if a == "":
    a = 'a'
#6
if len(a)>=16:
    a = a[:15]
    if a[-1] == '.':
        a = a[:-1]
#7
while len(a)<3:
    a +=a[-1]


print(a)
