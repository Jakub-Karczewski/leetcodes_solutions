class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(l, r, val):
            while l+1 < r:
                mid = (l+r)//2
                if numbers[mid] <= val:
                    l = mid
                else:
                    r = mid
            return l
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[right] + numbers[left] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:
                right = bin_search(left, right, target - numbers[left])
            else:
                prev_left = left
                left = bin_search(left, right, target - numbers[right])
                if numbers[right] + numbers[left] == target:
                    return [left + 1, right + 1]
                if prev_left == left:
                    left += 1
