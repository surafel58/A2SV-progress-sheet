# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.freq_map = defaultdict(int)

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        self.findTreeSum(root)

        maxFreq = max(self.freq_map.values())

        for key in self.freq_map:
            if self.freq_map[key] == maxFreq:
                result.append(key)



        return result

    def findTreeSum(self, root):

        if root == None:
            return 0

        left = self.findTreeSum(root.left)
        right = self.findTreeSum(root.right)

        total = left + right + root.val

        self.freq_map[total] += 1

        return total
