from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        """
        def partition(l, r, k, nums):
            piv_ind = r
            pivot = nums[piv_ind]
            #print(pivot)
            nums[piv_ind], nums[r] = nums[r], nums[piv_ind]
            bord = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[bord], nums[j] = nums[j], nums[bord]
                    bord += 1
            nums[r], nums[bord] = nums[bord], nums[r]

            if bord < k:
                for i in range(bord, k+1):
                    if nums[i] != pivot:
                        break
                    bord = i
            else:
                for i in range(bord, k-1, -1):
                    if nums[i] != pivot:
                        break
                    bord = i
            return bord
        def quick_select(l, r, k, nums):
            if l == r:
                return nums[l]
            pivot_index = partition(l, r, k, nums)
            print(pivot_index)
            if pivot_index == k:
                return nums[k]
            if pivot_index < k:
                quick_select(pivot_index + 1, r, k, nums)
            else:
                quick_select(l, pivot_index-1, k, nums)
        quick_select(0, len(nums) - 1, len(nums) - k, nums)
        return nums[len(nums) - k]
        """

        
        my_heap = PriorityQueue()
        for i in range(k):
            my_heap.put(nums[i])
        for i in range(k, len(nums)):
            low = my_heap.queue[0]
            if nums[i] > low:
                my_heap.get()
                my_heap.put(nums[i])
        return my_heap.queue[0]
