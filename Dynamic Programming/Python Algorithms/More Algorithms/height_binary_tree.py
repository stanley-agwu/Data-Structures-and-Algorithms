# Tree: Height of a Binary Tree

"""
The height of a binary tree is the number of edges between the tree's 
root and its furthest leaf. 

Write a function that returns a Tree's height, given the root node:
root: a reference to the root of a binary tree.

Note: In a binary search tree, all nodes on the left branch of a node 
    are less than the node value. All values on the right branch are 
    greater than the node value.
"""
# Note -The Height of binary tree with single node is taken as zero.

# Key Idea
"""
Since we are counting edges, the number of edges between n nodes is n - 1 edges.

Thus, in base cases instead of returning 0, we return -1
"""

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
# this is a node of the tree , which contains info as data, left , right

# Recursive solution
def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))
    
# Iterative solution
from collections import deque

def height(root):
    if root is None:
        return -1

    q = deque([root])
    h = -1

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        h += 1

    return h

# O(n) - Time complexity -> each Node visited once
# O(n) - Space complexity -> use of stack or Queue