"""
开幕式焰火, dfs
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numColor(self, root: TreeNode) -> int:
        ans = set()
        stack = [root,]
        while stack:
            temp = stack.pop()
            ans.add(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return len(ans)