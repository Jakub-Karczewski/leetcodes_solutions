class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters = dict()
        min_res = float('inf')
        best = [-1, -1]
        n = len(s)
        for x in t:
            letters[x] = letters.get(x, 0) + 1
        wanted = len(letters)
        if n <= 1:
            return s if s == t else ""
        l, r = 0, 1
        count = dict()
        count[s[0]] = 1
        fit = int(letters.get(s[0], 0) ==  1)
        if fit == wanted:
            return s[0]
        while r < n:
            count[s[r]] = count.get(s[r], 0) + 1
            if count[s[r]] == letters.get(s[r], 0):
                fit += 1
                if fit == wanted:
                    if r - l + 1 < min_res:
                        min_res = r - l + 1
                        best = l, r
                    while l <= r and fit == wanted:
                        if r - l + 1 < min_res:
                            min_res = r - l + 1
                            best = l, r
                        count[s[l]] -= 1
                        if letters.get(s[l]) is not None and count[s[l]] < letters[s[l]]:
                            fit -= 1
                        l += 1
            r += 1
        return s[best[0]:best[1]+1] if min_res != float('inf') else ""


