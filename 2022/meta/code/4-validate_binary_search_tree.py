class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(self, root: TreeNode):
    stack = []
    previous = float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= previous:
            return False
        previous = root.val
        root = root.right
    return True



