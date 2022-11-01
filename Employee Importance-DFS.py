#DFS
#Time Complexity:: O(n*s)-all nodes are visited in each level, and also their subordinates are visited
#Space Complexity:: O(n*s)-all the nodes and their subordinates importance are stored in an adjacency matrix
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        self.adj = {} #creating an adjacency matrix
        for emp in employees:
            self.adj[emp.id] = {"Value": emp.importance,"Subordinates": emp.subordinates} #creating adjacency matrix
            #For each employee storing their importance and subordinates
        result = self.records2(id)
        return result
    
    def records2(self,id): #traversing the records and adding the subordinates importance
        curr = self.adj[id]['Value']
        for sub in self.adj[id]['Subordinates']:
            curr = curr + self.records2(sub)
        return curr