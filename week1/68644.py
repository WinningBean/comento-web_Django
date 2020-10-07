def solution(numbers):  # 두 개 뽑아서 더하기
    answer = []
    for i, n in enumerate(numbers):
        for j in numbers[i + 1:]:  # numbers의 첫 요소와 그 다음 요소부터 numbers 모든 요소 반복
            answer.append(n + j)  # 요소 더하기

    answer = list(set(answer))  # set을 이용하여 중복 요소 제거
    answer.sort()  # 오름차순 정렬

    return answer