#DFS
#Time Complexity:: O(n)-all nodes are visited in each level and Null values are also process
#Space Complexity:: O(H)-a recursibe stack space is used

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right) #calling dfs recursion
        
    def dfs(self,leftnode, rightnode): #creating dfs function
        if not leftnode and not rightnode: #if both leftnode and rightnode are null return true
            return True

        if not leftnode or not rightnode: #if only node is null then return false
            return False

        if leftnode.val == rightnode.val: #if left node and right is palindromic then continue recursion
            return self.dfs(leftnode.left, rightnode.right) and self.dfs(leftnode.right, rightnode.left) #recursively call left subarray and right subarray

        return False

 

        