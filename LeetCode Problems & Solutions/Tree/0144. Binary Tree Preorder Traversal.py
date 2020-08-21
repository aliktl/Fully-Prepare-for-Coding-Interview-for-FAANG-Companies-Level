# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            answer = []
            if root:
                answer.append(root.val)
                answer+=dfs(root.left)
                answer+=dfs(root.right)
            return answer
        response = dfs(root)
        return response
            
            
            
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        if not root:
            return answer
        stack = []
        while root or stack:
            while root:
                answer.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return answer
