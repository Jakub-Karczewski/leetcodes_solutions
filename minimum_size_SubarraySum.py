class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_res = float('inf')
        n = len(nums)
        if n == 1:
            return int(nums[0] >= target)
        if n == 0:
            return 0
        if nums[0] >= target:
            return 1
        left, right, suma = 0, 1, nums[0]
        while right < n:
            suma += nums[right]
            if suma >= target:
                while left <= right and suma >= target:
                    min_res = min(min_res, right - left + 1)
                    suma -= nums[left]
                    left += 1
            right += 1
        return min_res if min_res != float('inf') else 0

        
