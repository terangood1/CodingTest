dt = ['FRI', 'SAT','SUN','MON','TUE','WED','THU']
num = [31,29,31,30,31,30,31,31,30,31,30,31]

a,b = list(map(int, input().split()))

k = sum(num[:a-1]) + b-1
print(dt[k%7])