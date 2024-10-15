def solution(players, callings):
    player = {player: i for i, player in enumerate(players)}

    for call in callings:
        n = player[call]
        players[n], players[n-1] = players[n-1], players[n]

        player[players[n]] = n
        player[players[n-1]] = n-1
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))