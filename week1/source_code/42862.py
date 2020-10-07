def solution(n, lost, reserve):  # 체육복
    clothes = [1] * n  # 전체 학생의 체육복

    for i in lost:
        clothes[i - 1] = 0  # 도난당한 학생의 체육복 제거
    for i in reserve:
        clothes[i - 1] += 1  # 여벌의 체육복을 가져온 학생의 체육복 추가

    for i, c in enumerate(clothes):
        if c > 1 and i != 0 and clothes[i - 1] == 0:  # 여벌의 체육복이 있으며 첫번째 번호가 아니고 앞번호 학생의 체육복이 없을 시
            clothes[i - 1] += 1  # 앞번호 학생에게 체육복 빌려주기
            c -= 1  # 해당 학생의 빌려준 체육복 제거
        if c > 1 and i != n - 1 and clothes[i + 1] == 0:  # 여벌의 체육복이 있으면 마지막 번호가 아니고 뒷번호 학생의 체육복이 없을 시
            clothes[i + 1] += 1  # 뒷번호 학생에게 체육복 빌려주기
            c -= 1  # 해당 학생의 빌려준 체육복 제거

    return n - clothes.count(0)  # 체육수업을 들을 수 있는 학생 수