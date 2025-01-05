class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            x = i ** 2
            ans.append(x)
        ans.sort()
        return ans