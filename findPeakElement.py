def findPeakElement(self, nums: List[int]) -> int:
        
        
        i = 1
        
        for i in range(len(nums) -1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        
        return len(nums) - 1
