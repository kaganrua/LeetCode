def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def fun(l):
            if not l:
                return []
            tmp = set()
            for i in range(len(l)):
                for item in fun(l[:i] + l[i+1:]):
                    tmp.add(tuple(item))
            tmp.add(tuple(l))
            return list(tmp)
        
        sol = fun(nums)
        sol.append([])
        
        return sol
