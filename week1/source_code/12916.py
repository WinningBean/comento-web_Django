def solution(s):  # 문자열 내 p와 y의 개수
    pCount = yCount = 0  # p와 y의 개수 초기화

    for i in s:
        if i == 'p' or i == 'P':
            pCount += 1
        if i == 'y' or i == 'Y':
            yCount += 1

    return pCount == yCount  # p와 y의 개수가 같다면 True 아니라면 False