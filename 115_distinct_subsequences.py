class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 for _ in range(len(t))]
        positions_in_word = dict()
        for i, letter in enumerate(t):
            lst = positions_in_word.get(letter, [])
            lst.append(i)
            positions_in_word[letter] = lst
        ind = 0
        for i in range(len(s)):
            letter = s[i]
            if len(positions_in_word.get(letter, [])):
                for k in positions_in_word[letter][::-1]:
                    if k == 0:
                        dp[0] += 1
                    else:
                        dp[k] += dp[k-1]
        return dp[-1]
