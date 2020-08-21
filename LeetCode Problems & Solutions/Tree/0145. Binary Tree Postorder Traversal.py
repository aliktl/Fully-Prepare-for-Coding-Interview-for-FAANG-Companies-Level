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
        
  Explanation: 
    1)Postorder meaning: left, right, root
    2) So we just make recursion function for going to the all nodes
    3) Make empty list and go through all nodes with postorder traversal and append the root.val 
     
        
        
        
        
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
    
    
    
    Explanation:
  1) This is iterative solution
  2) Initially we check if there is a root or empty input
  3) Create stack for using it in the while loop together with root inside
  4) If stack is empty, we stop and return asnwer
  5) While there is node in stack (stack is not empty), we pop the node from the stack
  6) If the node is not empty, we append the value of this node to the answer
  7) Lastly, we append the left and right nodes in the stack
  8) The idea is to make reversed list , like root, right, left and reverse it in the end
    
    
    
    
    
    
    
    
