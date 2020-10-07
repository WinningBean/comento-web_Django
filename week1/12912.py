def solution(a, b):  # 두 정수 사이의 합
    if a > b:  # a보다 b가 더 큰 수라면 두 수 교환
        temp = a
        a = b
        b = temp

    count = a - b  # 두 정수 사이의 정수의 개수 - 1
    if count < 0:  # 음수라면 양수로 변환
        count = -count

    answer = a * (count + 1)  # 작은 수 * 두 정수 사이의 정수의 개수
    answer += (count + 1) * count // 2  # 두 정수 사이의 정수의 개수 * count(이미 계산된 a를 제외한 정수의 개수) // 2

    return answer