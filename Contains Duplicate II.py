class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and abs(i - (i-1)) <= k:
                return True

        return False