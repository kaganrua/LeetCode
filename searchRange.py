def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        last = -1
        first = -1
        
        i = len(nums) - 1
        j = 0
        
        
        for i in range(len(nums)):
            if nums[i] == target and first == -1:
                first = i
            if nums[i] == target:
                last = i
        
        return [first,last]
