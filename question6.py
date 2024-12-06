#6. 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다.

#각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
#신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
#한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.

#k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
#유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

user_id = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2 #제재 기준

def validation_length(user_id, report): #
    if not 2<=len(user_id)<=1000:
        raise ValueError("리스트의 전체 길이는 2 이상 1000이하여야 합니다.")

    for elem in user_id:
        if not 1<=len(str(elem))<=10:
            raise ValueError("리스트의 원소 길이는 1글자 이상 10글자 이하여야 합니다.")
        
    if not 1<=len(report)<=200000:
        raise ValueError("리스트의 전체 길이는 1 이상 200000이하여야 합니다.")

    for elem in report:
        if not 3<=len(str(elem))<=21:
            raise ValueError("리스트의 원소 길이는 3글자 이상 21글자 이하여야 합니다.")
        
    return True

def solution(user_id, report, k):
    report = set(report) #list는 중복 데이터 O / set은 중복 데이터 X 이기 때문에 중복 신고를 제거하기 위해 set 사용

    report_count = {user: 0 for user in user_id} #신고 카운팅 0으로 초기화
    user_report = {user: [] for user in user_id} #신고 내역 초기화

    for entry in report: #entry를 이용해 딕셔너리 내의 문자열 순회
        reporter, reported = entry.split() #split으로 공백 기준 나누기
        user_report[reporter].append(reported)
        report_count[reported] += 1

        print(f'"{reporter}"가 {reported}를 신고했습니다.') #신고 메일

    banned_user = {user for user, count in report_count.items() if count >= k}

    for user, count in report_count.items():
        print(f"{user}는 {count}번 신고 당했습니다.") #신고 횟수

    print(f"정지 당한 사람 : {banned_user}")

    result = []
    for user in user_id:
        mail_count = sum(1 for reported in user_report[user] if reported in banned_user)
        result.append(mail_count)

    return result

if __name__ == "__main__":
    validation_length(user_id, report)
    print(f"사용자 목록 : {user_id}")
    print(solution(user_id, report, k))