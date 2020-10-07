def solution(participant, completion):  # 완주하지 못한 선수
    p = set(participant)  # 참여한 선수 동명이인 제거
    c = set(completion)  # 완주한 선수 동명이인 제거
    result = (list(p - c))  # 완주하지 못한 선수 추출

    if len(result) == 1:  # 완주한 선수가 추출됐다면 (한명이라면)
        answer = result[0]  # 완주하지 못한 선수는 해당 선수
    else:  # 동명이인이 완주하지 못한 선수일 경우
        pDic = {}  # 참여한 선수 딕셔너리
        cDic = {}  # 완주한 선수 딕셔너리

        for i in participant:  # pDic key-value
            try:
                pDic[i] += 1
            except:
                pDic[i] = 1

        for i in completion:  # cDic key-value
            try:
                cDic[i] += 1
            except:
                cDic[i] = 1

        for key in pDic:
            if pDic[key] != cDic[key]:  # 해당 선수의 value값이 다르다면
                answer = key  # 해당 선수가 완주하지 못한 선수 (동명이인)

    return answer