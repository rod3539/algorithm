def solution(players, callings):
    rankDic = {}
    playerDic = {}

    for idx, player in enumerate(players):
        rankDic[idx + 1] = player
        playerDic[player] = idx + 1

    for cur_player in callings:
        cur_rank = playerDic[cur_player]
        prev_rank = cur_rank - 1
        prev_player = rankDic[prev_rank]

        rankDic[cur_rank - 1], rankDic[cur_rank] = rankDic[cur_rank], rankDic[cur_rank - 1]
        playerDic[prev_player], playerDic[cur_player] = playerDic[cur_player], playerDic[prev_player]


    return list(rankDic.values())