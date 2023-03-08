# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        treeVal_freq = defaultdict(int)
        maxFreq = 0
        result = []

        def getNodes(root):
            nonlocal maxFreq

            if root:

                treeVal_freq[root.val] += 1
                maxFreq = max(maxFreq, treeVal_freq[root.val])

                left = getNodes(root.left)
                right = getNodes(root.right)
        
        getNodes(root)


        for key in treeVal_freq:
            if treeVal_freq[key] == maxFreq:
                result.append(key)
        
        return result
            
