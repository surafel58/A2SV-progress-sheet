class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #colliding pointers
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if limit >= people[left] + people[right]:
                left += 1
                
            right -= 1
            boats += 1

        return boats 
