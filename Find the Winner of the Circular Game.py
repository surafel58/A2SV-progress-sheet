class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        for num in range(1, n + 1):
            players.append(num)
        start = 0
        while len(players) > 1:
            length = len(players)
            players.pop((start + k - 1) % len(players))
            start = (start + k - 1) % length

        return players[0]
