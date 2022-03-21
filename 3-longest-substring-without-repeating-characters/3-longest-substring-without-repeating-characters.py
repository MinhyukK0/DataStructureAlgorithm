class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        max_len = 0
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            max_len = max(max_len, idx - start + 1)
            used[char] = idx
        return max_len