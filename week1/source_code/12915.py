def solution(strings, n):  # 문자열 내 마음대로 정렬하기
    answer = []
    sortList = [i[n] for i in strings]  # n번째 정렬기준 리스트
    sortList.sort()  # 정렬기준 리스트를 정렬
    strings.sort()  # 문자열 리스트 사전순으로 정렬

    for i in sortList:  # 정렬기준으로 반복해야 원하는 대로 정렬 가능
        for j in strings:
            if i == j[n]:  # 정렬기준과 문자열 리스트의 n번째 요소가 같다면
                answer.append(j)  # 답에 해당 문자열을 추가
                strings.remove(j)  # 문자열 리스트에서 답에 추가된 문자열 삭제 - 다음애 중복될 수 있으므로
                break

    # 다른 사람의 풀이에서 sorted() 함수를 사용해 lambda 표현 - 기억하기
    # sorted(strings, key=lambda x: x[n])
    # 이를 튜플에 활용하면
    # sorted(student_tuples, key=lambda student: student[2])
    # 위는 학생들의 정보 튜플을 인덱스 2번째 요소로 정렬하는 코드 (예를 들어 나이 인덱스를 기준으로)
    # sorted(student_tuples, key=itemgetter(2), reverse=True)
    # 위 코드처럼 reverse 매개변수를 True로 하여 내림차순(뒤집기)으로 정렬도 가능 (list.sort() 에서도 가능하다)

    return answer