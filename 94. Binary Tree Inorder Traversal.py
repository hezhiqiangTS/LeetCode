# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal_withRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
            
        result=[]
        
        left=self.inorderTraversal(root.left)
        if left:
            result+=left
                
        result.append(root.val)
        
        right=self.inorderTraversal(root.right)
        if right:
            result+=right
                   
        return result



    def inorderTraversal_withoutRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        
        cur=root
        S=Stack()
        result=[]
        
        while(cur):
            S.push(cur)        
            cur=cur.left
            
        cur=S.top()
        
        while(not S.is_empty()):
            cur=S.pop()
            
            if cur.right is None:
                result.append(cur.val)
            else:
                result.append(cur.val)
                cur=cur.right
                while(cur):
                    S.push(cur)
                    cur=cur.left
                    
        return result

class Stack():
    def __init__(self):
        self._data=[]

    def is_empty(self):
        return len(self._data)==0
    
    def push(self,e):
        self._data.append(e)
      
    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()
    
    def top(self):
        if self.is_empty():
            return None
        return self._data[-1]
    
    
    
    
    
    
    
    
    
    
    
    
        