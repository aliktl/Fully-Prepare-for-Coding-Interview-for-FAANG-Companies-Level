# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            answer = []
            if root:
                answer+=dfs(root.left)
                answer+=dfs(root.right)
                answer.append(root.val)
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        if not root:
            return answer
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                answer.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return answer[::-1]
