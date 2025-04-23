from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        """
        Sposób 1
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
            nums[r], nums[bord] = nums[bord], nums[r]22

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

        """
        Sposób 2
        my_heap = PriorityQueue()
        for i in range(k):
            my_heap.put(nums[i])
        for i in range(k, len(nums)):
            low = my_heap.queue[0]
            if nums[i] > low:
                my_heap.get()
                my_heap.put(nums[i])
        return my_heap.queue[0]
        """

        #Sposób 3
        my_dict = dict()
        my_heap = PriorityQueue()
        for x in nums:
            my_dict[x] = my_dict.get(x, 0) + 1
        act_capacity = 1
        vals = list(my_dict.items())
        my_heap.put((vals[0][0], vals[0][1]))
        for i in range (1, len(vals)):
            print(my_heap.queue)
            if act_capacity + vals[i][1] > k:
                if vals[i][0] > my_heap.queue[0][0]:
                    el, c = my_heap.get()
                    act_capacity -= c
                    while not my_heap.empty() and act_capacity - my_heap.queue[0][1] + vals[i][1] >= k and my_heap.queue[0][0] < vals[i][0]:
                        x, y = my_heap.get()
                        act_capacity -= y
                    my_heap.put((vals[i][0], vals[i][1]))
                    act_capacity += vals[i][1]
            else:
                my_heap.put((vals[i][0], vals[i][1]))
                act_capacity += vals[i][1]
        return my_heap.queue[0][0]
