
#결과 저장
result = 0
# 단어를 받는다
word = input()
# 중복제거한 알파벳만 따로 리스트 구현
word_list = list(set(word))

#단어에 있는게 중복제거한것과 비교하는 for문
for i in word_list:
    count = []
    k = 0
    for j in word:
        if i == j:
            print(i, j)
            count.append(k*0)
        else:
            print(i, j)
            count.append(k+1)
    print(count)

        
#카운트 같으면 곱하기0 다르면 더하기 1

#0보다 크면 결과에 1추가 


