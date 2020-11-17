# Given preorder and inorder traversal of a tree, construct the binary tree.

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
  
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder or not inorder:
            return None 
        root = TreeNode(preorder[0])
        rootPosition = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+rootPosition], inorder[:rootPosition])
        root.right = self.buildTree(preorder[1+rootPosition:], inorder[rootPosition +1:])
        return root