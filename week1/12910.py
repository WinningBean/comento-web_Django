def solution(arr, divisor):  # 나누어 떨어지는 숫자 배열
    answer = [i for i in arr if i % divisor == 0]  # arr의 요소가 divisor로 나누어 떨어지는 경우 정답에 추가
    answer.sort()  # 오름차순 정렬
    if len(answer) < 1:  # 나누어ㄷ 떨어지는 숫자가 없다면
        answer.append(-1)

    return answer