def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        Q = [root]
        
        cur_level = 1
        next_level = 0
        
        def BFS(root):
            nonlocal cur_level
            nonlocal next_level
            
            if root:
                
                while Q:
                    cur_node = Q.pop(0)
                    cur_level -= 1
                    if cur_node.left:
                        Q.append(cur_node.left)
                        next_level += 1
                    if cur_node.right:
                        Q.append(cur_node.right)
                        next_level += 1
                    if cur_level == 0:
                        nodes.append(cur_node.val)
                        cur_level = next_level
                        next_level = 0
        BFS(root)
        return nodes
