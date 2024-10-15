def solution(players, callings):
    for i in range(len(callings)):
        n = players.index(callings[i])
        players[n], players[n-1] = players[n-1], players[n]
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))