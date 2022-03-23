 def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        sol = []
        for num in nums1:
            if num in nums2:
                sol.append(num)
        
        return sol
