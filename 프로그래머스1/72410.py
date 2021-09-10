word = ['zero','one','two','three','four', 'five','six','seven','eight','nine']

a = input()

for i in range(len(word)):
    if word[i] in a:
        a = a.replace(word[i],str(word.index(word[i])))


print(int(a))
