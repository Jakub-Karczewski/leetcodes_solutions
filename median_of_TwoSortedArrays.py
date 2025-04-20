class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def binsearch(arr, l, r, val):
            while l + 1 < r:
                mid = (l + r) // 2
                if arr[mid] <= val:
                    l = mid
                else:
                    r = mid
            return l if arr[l] <= val else -1
        if not len(nums1):
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2)//2-1] + nums2[len(nums2)//2])/2
            else:
                return nums2[len(nums2)//2]
        if not len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        target = (len(nums1) + len(nums2) + 1) // 2
        ind1 = len(nums1) // 2
        ind2 = target - ind1 - 2
        while True:
            val1 = nums1[ind1] if ind1 >= 0 else -float('inf')
            val2 = nums2[ind2] if ind2 >= 0 else -float('inf')
            if val1 < val2:
                if ind1 + 1 == len(nums1):
                    break
                if (val1 == -float('inf') and nums1[ind1 + 1] == val2):
                    break
                if nums1[ind1 + 1] < val2:
                    ind2 = binsearch(nums2, 0, ind2, nums1[ind1 + 1])
                    ind1 = target - ind2 - 2
                    if ind1 >= len(nums1):
                        ind1 = len(nums1) - 1
                        ind2 = target-ind1 - 2
                else:
                    break
            elif val1 > val2:
                if ind2 + 1 == len(nums2):
                    break
                if (val2 == -float('inf') and nums2[ind2 + 1] == val1):
                    break
                if nums2[ind2 + 1] < val1:
                    ind1 = binsearch(nums1, 0, ind1, nums2[ind2 + 1])
                    ind2 = target - ind1 - 2
                    if ind2 >= len(nums2):
                        ind2 = len(nums2) - 1
                        ind1 = target-ind2 - 2
                else:
                    break
            else:
                break
        if (len(nums1) + len(nums2)) % 2 == 1:
            if ind1 == -1:
                return nums2[ind2]
            if ind2 == -1:
                return nums1[ind1]
            return max(nums1[ind1], nums2[ind2])
        else:
            val1, val2 = nums1[ind1 + 1] if ind1 + 1 < len(nums1) else float('inf'), nums2[ind2 + 1] if ind2 + 1 < len(nums2) else float('inf')
            if ind1 == -1:
                return (nums2[ind2] + min(val1, val2))/2
            if ind2 == -1:
                return (nums1[ind1] + min(val1, val2))/2
            else:
                return (max(nums1[ind1], nums2[ind2]) + min(val1, val2)) / 2
            

        
        
