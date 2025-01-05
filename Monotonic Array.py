class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in nums:
                if j < (j+1) or j > (j+1):
                    return False
        return True
                    
