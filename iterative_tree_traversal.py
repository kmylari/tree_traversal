from typing import Optional
# Online Python - IDE, Editor, Compiler, Interpreter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: Optional[TreeNode]):
    if not root:
        return
    queue = []
    queue.append(root)
    while queue:
        n = queue.pop(0)
        print(n.val, end="")
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    print()

def dfspre(root: Optional[TreeNode]):
    if not root:
        return
    stack = [root]
    while stack:
        n = stack.pop()
        print(n.val, end="")
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
        
    print()
        
    
def dfspost(root:  Optional[TreeNode]):
    if not root:
        return
    stack = [root]
    postorder = []
    while stack:
        cur = stack.pop()
        postorder.append(cur)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    while postorder:
        print(postorder.pop().val, end="")
    print()

def dfsin(root:  Optional[TreeNode]):
    cur = root
    stack = []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur=cur.left
        cur = stack.pop()
        print(cur.val, end="")
        cur = cur.right
    print()
    
    
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    print("*" * 5, "levelorder", "*" * 5)
    bfs(root)
    print("*" * 5, "preorder", "*" * 5)
    dfspre(root)
    print("*" * 5, "postorder", "*" * 5)
    dfspost(root)
    print("*" * 5, "inorder", "*" * 5)
    dfsin(root)