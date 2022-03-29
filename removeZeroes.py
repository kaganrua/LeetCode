def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for element in nums:
            if element == 0:
                nums.remove(element)
                nums.append(element)
