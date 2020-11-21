"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        self.findP=False
        return self.inordertraversal(root,p)
        
        
    def inordertraversal(self,root, p):
        if root is None:
            return None
        # print(root.val, self.findP)
        result = self.inordertraversal(root.left, p)
        if result:
            return result
        if self.findP:
            return root
        if root.val == p.val:
            self.findP = True
        return self.inordertraversal(root.right, p)
        
