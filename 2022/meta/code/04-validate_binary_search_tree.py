class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(self, root: TreeNode):
    stack = []
    previous = float('-inf')
    # because we need make sure stack and root is not none(out of bound)
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

    # def dfs(root,max,min):
    #         if root is None:
    #             return True
    #         if root.val >=max or root.val <=min:
    #             return False
            
    #         return dfs(root.left,root.val,min) and dfs(root.right,max,root.val)
        
    #     return dfs(root,float('inf'), float('-inf'))
        



