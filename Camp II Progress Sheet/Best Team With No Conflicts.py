class Players:
    def __init__(self, age, score):
        self.age = age
        self.score = score

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        players = [Players(ages[i], scores[i]) for i in range(len(scores))]
        players.sort(reverse=True, key=lambda a : (a.age, a.score))
        memo = dict()
        def dp(prevScore, i):

            if i >= len(scores):
                return 0
            
            if (prevScore, i) in memo:
                return memo[(prevScore, i)]

            ans = 0
            if players[i].score > prevScore:
                ans =  dp(prevScore, i + 1)
            else:
                ans = max(dp(prevScore, i + 1), players[i].score + dp(players[i].score, i + 1))

            memo[(prevScore, i)] = ans

            return memo[(prevScore, i)]

        result = 0
        for i in range(len(players)):
            result = max(result, dp(2**31 - 1, i))
        
        return result
