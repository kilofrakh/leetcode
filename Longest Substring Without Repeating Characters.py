class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if len(set(s[i:j])) == j-i:
                    counter = max(counter, j-i)
        return counter