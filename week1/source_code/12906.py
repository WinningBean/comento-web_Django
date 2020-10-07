def solution(arr):  # 같은 숫자는 싫어
    pre = arr[0]  # arr의 첫번째 요소로 이전 숫자 초기화
    answer = [pre]  # 정답에 pre로 초기화

    for i in arr:
        if pre != i:  # 현재 숫자가 이전 숫자와 다르다면
            answer.append(i)  # 정답에 현재 숫자 추가
            pre = i  # 이전 숫자를 현재 숫자로 변경

    return answer