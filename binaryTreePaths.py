def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def recursive(root, l, ans):
            if not root:
                return
            l += str(root.val) + "->"
            recursive(root.left,l,ans)
            recursive(root.right, l, ans)
            if not root.left and not root.right:
                
                ans.append(l[:-2])
            return ans
        return recursive(root, "",[])
