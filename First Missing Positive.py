class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()  # Sort the array
        numToBeAt = 1
        
        for num in nums:
            if num < 1:
                continue
            if num == numToBeAt:
                numToBeAt += 1
            elif num > numToBeAt:
                return numToBeAt
        
        return max(nums[-1] + 1, 1)