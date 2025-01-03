class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        while True:
            if val in nums:
                count += 1
                nums.remove(val)
            else:
                break
        
        