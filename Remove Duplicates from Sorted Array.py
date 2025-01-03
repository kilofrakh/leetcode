class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set1= set(nums)
        nums.clear()
        nums.extend(set1)
        nums.sort()