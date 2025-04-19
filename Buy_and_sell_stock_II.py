class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, res = len(prices), 0
        if n <= 1:
            return 0
        i, temp_min = 1, prices[0]
        while( i < n):
            if prices[i] < prices[i-1]:
                while i < n and prices[i] < prices[i-1]:
                    i += 1
                temp_min = prices[i-1]
            else:
                while i < n and prices[i] >= prices[i-1]:
                    i += 1
                res += prices[i-1] - temp_min
        return res
