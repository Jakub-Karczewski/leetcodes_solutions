class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        left, right, max_res = 0, 1, 0
        letters = [0] * 128
        letters[ord(s[left])] = 1
        while right < n:
            if letters[ord(s[right])] == 1:
                while left < right and letters[ord(s[right])] == 1:
                    letters[ord(s[left])] = 0
                    left += 1
            letters[ord(s[right])] = 1
            max_res = max(right - left+1, max_res)
            right += 1
        return max_res
