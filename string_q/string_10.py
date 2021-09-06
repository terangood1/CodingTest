
#결과 저장
result = 0
# 단어를 받는다
word = input()
# 중복제거한 알파벳만 따로 리스트 구현
word_list = list(set(word))

#단어에 있는게 중복제거한것과 비교하는 for문
for i in word_list:
    count1 = []
    k = 0
#중복이면 0 아니면 1
    for j in word:
        if i == j:
            count1.append(0)
        else:
            count1.append(1)
    print(count1)
#0이 2개이상이면 그 두개의 위치가 붙어있는지 확인
    if count1.count(0) > 1:
        print(count1.count(0))
        for i in count1:
            print(count1.index(i))




