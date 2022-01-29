from collections import Counter

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

id_list = ["muzi", "frodo", "apeach", "neo"]

k = 2

answer = []
check_list = []
report_dict = {}

for report_id in id_list:
    report_dict[report_id] = []
    
for case in report:
    report_id, report_name = case.split()
    #중복제거 밑 정리
    if report_name not in report_dict[report_id]:
        report_dict[report_id].append(report_name)
        #신고당한 사람
        check_list.append(report_name)
        
#같은 이름이 몇개 나왔는지 카운트 해줌 신고당한 사람 카운트
cnt_dict = Counter(check_list)
#횟수 찾기
for report_id in id_list:
    count = 0
    for check in report_dict[report_id]:
        if cnt_dict[check]>=k:
            count += 1
    answer.append(count)