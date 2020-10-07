def solution(s):  # 가운데 글자 가져오기
    l = len(s)  # 단어 s의 길이
    if l % 2 == 0:  # 짝수라면
        answer = s[int(l / 2) - 1] + s[int(l / 2)]  # 가운데 두 글자
    else:  # 홀수라면
        answer = s[int(l / 2 - 0.5)]  # 가운데 한 글자

    return answer