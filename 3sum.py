#Zamiast zwiększania left/right tylko o 1 lub o tyle ile razy występuje pod rząd, można użyć binsearcha, wtedy jest dużo lepsza złożoność
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n <= 2:
            return res
        nums.sort()
        i = 0
        while i < n-2:
            wanted, temp = -nums[i], nums[i]
            left, right = i+1, n-1
            if nums[left] == nums[right]:
                if 2 * nums[left] == wanted:
                    res.append([nums[i], nums[left], nums[left]])
                return res
            while left < right:
                if nums[left] == nums[right]:
                    if 2 * nums[left] == wanted:
                        res.append([nums[i], nums[left], nums[left]])
                    break
                if nums[left] + nums[right] > wanted:
                    prev_right = right
                    while left < right and nums[right] == nums[prev_right]:
                        right -= 1
                    if prev_right - right >= 2 and 2 * nums[prev_right] == wanted:
                        res.append([nums[i], nums[prev_right], nums[prev_right]])
                else:
                    prev_left = left
                    while left < right and nums[left] == nums[prev_left]:
                        left += 1
                    if nums[prev_left] + nums[right] == wanted:
                        res.append([nums[i], nums[prev_left], nums[right]])
                    if 2 * nums[prev_left] == wanted:
                        res.append([nums[i], nums[prev_left], nums[prev_left]])
            while i < n-2 and nums[i] == temp:
                i += 1
        return res
