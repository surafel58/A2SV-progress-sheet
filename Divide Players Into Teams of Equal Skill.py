class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        totalSum = sum(skill)
        teamsAmount = len(skill) / 2

        #needed skill for each team - target sum
        teamSkill = totalSum / teamsAmount

        chemistry = 0

        skill.sort()

        left = 0
        right = len(skill) - 1

        while left < right:
            if teamSkill != skill[left] + skill[right]:
                return -1
            else:
                chemistry += (skill[left] * skill[right])
                left += 1
                right -= 1

        return chemistry



    
