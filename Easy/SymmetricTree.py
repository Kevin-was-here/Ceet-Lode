"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
from turtle import right


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSymmetric(self, root) -> bool:
    def isSym(L,R):
        if not L and not R: return True
        if L and R and L.val == R.val: 
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return False
    return isSym(root, root)
      

def main():
  root = TreeNode(0,None,3)
  print(Solution.isSymmetric(root))

if __name__ == "__main__":
  main()
