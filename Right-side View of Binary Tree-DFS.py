#DFS
#Time Complexity:: O(n)-all nodes are visited in each level and Null values are also process
#Space Complexity:: O(n)-a result dictionary is required to store all rightmost nodes in each level

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        self.result = {} #using DFS for traversing
        self.recur(root,0) #height is initialized to 0 with first root node
        return list(self.result.values())  #values inside the hashmap is return
        
    def recur(self,root,height): 
        #Base 
        if root == None: #if null node detected just return
            return
        
        #Logic
        self.recur(root.left,height+1) #everytime you go into a child node add to the height
        self.recur(root.right,height+1)
           
        self.result[height]=root.val #use the current height as the key and assign the last node in that level into the dictionary as a value
        
        return #no need to return anything, can also be used to return height
