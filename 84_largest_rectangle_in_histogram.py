class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        res = 0
        for i in range(len(heights)):
            h = heights[i]
            count = 0
            while len(stack) and stack[-1][0] > h:
                count += stack[-1][1]
                res = max(res, stack[-1][0] * count)
                stack.pop()
            stack.append([h, count+1])
        return res
