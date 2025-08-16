class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        max_left, max_right = height[0], height[n-1]
        left, right = 0, n-1
        while left < right:
            if height[left] < height[right]:
                if height[left] < max_left:
                    res += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if height[right] < max_right:
                    res += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        return res

        
