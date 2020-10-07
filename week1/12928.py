def solution(n):  # 약수의 합
    answer = 0  # 정답 초기화
    for i in range(1, n + 1):  # 1부터 n까지 반복
        if n % i == 0:  # 약수라면
            answer += i  # 정답에 약수 더하기

    return answer