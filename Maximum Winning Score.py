#structure of class Node
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def dfs(self, node, c):
        if node == None:
            return c
        c *= node.data
        f = max(self.dfs(node.left, c), self.dfs(node.right, c))
        c /= node.data
        return f
        
        
        
            
    def findMaxScore(self, root):
        #code
        c = 1
        e = self.dfs(root, c)
        return e
        
        
