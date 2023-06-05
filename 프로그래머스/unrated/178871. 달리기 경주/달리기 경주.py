def solution(players, callings):
    players_index = {players[i]: i for i in range(len(players))}
    for call in callings:
        index = players_index[call]
        players_index[players[index]], players_index[players[index - 1]] = index - 1, index
        players[index], players[index - 1] = players[index - 1], players[index]
    return players