class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        used_char = {}
        for i, char in enumerate(s):
            if char in used_char and start <= used_char[char]:
                start = used_char[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used_char[char] = i
        return max_length