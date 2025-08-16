class Solution:
    result = -inf

    def solve(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            self.result = max(self.result, root.val)
            return root.val

        left = self.solve(root.left) if root.left else -inf
        right = self.solve(root.right) if root.right else -inf
        self.result = max(self.result, root.val, root.val + max(0, left) + max(0, right))

        return max(root.val + max(0, left), root.val + max(0, right)) 

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return max(root.val, self.result)
