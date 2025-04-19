class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        k = 2 * numRows - 2
        res = ""
        for i in range(numRows):
            if i >= len(s):
                return res
            pos = i + k
            res += s[i]
            while pos - 2 * i < len(s):
                if i == 0 or i == numRows - 1:
                    res += ( s[pos] if pos < len(s) else "")
                else:
                    res += s[pos - 2 * i]
                    res += ( s[pos] if pos < len(s) else "")
                pos += k
        return res

        
