def solution(answers):  # 모의고사
    supo1 = [1, 2, 3, 4, 5]  # 1번 수포자가 찍는 방식
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 2번 수포자가 찍는 방식
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번 수포자가 찍는 방식
    result = [0, 0, 0]  # 각 수포자들 맞힌 문제 개수
    count = [len(supo1), len(supo2), len(supo3)]  # 각 수포자들의 찍는 방식 길이 (pattern Loop)

    for i, a in enumerate(answers):  # 모의고사 문제만큼 반복
        if a == supo1[i % count[0]]:  # 1번 수포자의 찍는 방식의 답과 정답이 같다면 (모의고사 문제번호에 pattern Loop를 적용하여 수포자의 찍는 답 추출)
            result[0] += 1  # 해당 수포자의 맞힌 문제 개수 증가
        if a == supo2[i % count[1]]:  # 2번 수포자
            result[1] += 1
        if a == supo3[i % count[2]]:  # 3번 수포자
            result[2] += 1

    maxResult = max(result)  # 가장 많이 맞힌 문제

    return [i + 1 for i, r in enumerate(result) if maxResult == r]  # result의 요소가 maxResult와 같다면 가장 많은 문제를 맞힌 사람에 추가