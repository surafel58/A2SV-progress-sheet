class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        changes = {5 :0, 10: 0}
        
        countMoney = 0

        for bill in bills:

            if bill == 5:
                changes[bill] += 1
            
            if bill == 10:
                changes[bill] += 1
                changes[5] -= 1

            elif bill == 20:
                
                if changes[10] > 0:
                    changes[10] -= 1
                else:
                    changes[5] -= 2

                changes[5] -= 1
                
            if changes[5] < 0 or changes[10] < 0:
                return False
                
        return True
