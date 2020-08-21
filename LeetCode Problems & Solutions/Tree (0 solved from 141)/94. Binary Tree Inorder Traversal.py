# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            answer = []
            if root:
                answer += dfs(root.left)
                answer.append(root.val)
                answer += dfs(root.right)
            return answer
        response = dfs(root) 
        return response
        
        
Explanation:
  1) Inorder meaning: left, root, right
  1-1) Inorder tree traversal is a type of depth first search (DFS) where we explore tree nodes in a particular order: left, root, right.
  2) So we just make recursion function for going to the all nodes
  3) Make empty list and go through all nodes with inorder traversal and append the root.val 


  
  
  
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
        
        
        
Explanation:
  1) This is iterative solution
  2) Initially we check if there is a root or empty input
  3) Create stack for using it in the while loop
  4) If stack and root are empty, we stop and return asnwer
  5) While there is root.left (left root is not None), we append the root to stack
  6) When there are no more root lefts, we append the value of that root, and check for the root.right
  7) The idea is to go to the left until you can, and when finished, go the the right, and again check for the all left roots

        
        

      
      
      
