def solution(array, commands):  # K번째수
    answer = []

    for c in commands:
        resultArray = array[c[0] - 1: c[1]]  # 배열의 첫번째 번호부터 두번째 번호까지 array를 슬라이싱
        resultArray.sort()  # 결과 정렬
        answer.append(resultArray[c[2] - 1])  # K번째 수 정답으로 추가

    return answer