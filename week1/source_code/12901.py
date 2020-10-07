def solution(a, b):  # 2016년
    DoW = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]  # 일요일부터 토요일
    day = 5  # 2016년의 시작하는 요일 초기화 (금요일)

    for i in range(1, a):  # 1월부터 a달 전달까지 날짜 계산
        if i in (1, 3, 5, 7, 8, 10, 12):  # 해당 달이면
            day += 31  # 31일 추가
        elif i in (4, 6, 9, 11):  # 해당 달이면
            day += 30  # 30일 추가
        else:  # 2월이라면
            day += 29  # 29일 추가 (2016년은 윤년)

    day += b  # 날짜에 현재 날짜 추가
    week = day % 7  # 현재 날짜 일주일 단위로 계산

    return DoW[week - 1]