def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0:
            return None
        
        rootVal = preorder[0]
        
        root = TreeNode(rootVal)
        
        rootIndex = -1
        
        for i in range(len(inorder)):
            if inorder[i] == rootVal:
                rootIndex = i
                break
        
        
        if rootIndex == -1:
            return None
        
        leftind = inorder[:rootIndex]
        rightind = inorder[rootIndex+1:]
        
        leftpre = preorder[1 : len(leftind) + 1]
        rightpre = preorder[len(leftind) + 1:]
        
        root.left =  self.buildTree(leftpre, leftind)
        root.right = self.buildTree(rightpre, rightind)
        
        return root
