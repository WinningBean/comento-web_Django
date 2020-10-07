def solution(board, moves):  # 크레인 인형뽑기 게임
    answer = 0  # 사라진 인형
    result = []  # 결과 바구니
    nowResult = 0  # 현재 크레인의 결과

    for m in moves:
        for w in board:
            if w[m - 1] != 0:  # 크레인의 위치에 인형이 있다면
                nowResult = w[m - 1]  # 현재 크레인이 잡고있는 인형
                w[m - 1] = 0  # 인형이 있던 칸은 비워진다
                if len(result) > 0 and result[-1] == nowResult:  # 결과 바구니에 있는 인형이 하나 이상이며 결과 바구니의 마지막 인형과 현재 크레인 인형이 같다면
                    del result[-1]  # 바구니의 마지막 인형을 터트린다
                    answer += 2  # 사라진 인형에 터트려진 인형 수를 더한다 (바구니 마지막 인형 + 크레인 인형)
                    break
                result.append(nowResult)  # 인형이 터트려지지 않으면 결과 바구니에 쌓이게 된다
                break

    return answer
