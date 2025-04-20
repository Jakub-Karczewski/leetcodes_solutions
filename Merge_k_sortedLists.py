from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_heap = PriorityQueue()
        res_list = None
        for i in range(len(lists)):
            if lists[i] != None:
                my_heap.put((lists[i].val, i))
        first_node = None
        while not my_heap.empty():
            val, id = my_heap.get()
            if res_list == None:
                res_list = ListNode(val)
                first_node = res_list
            else:
                res_list.next = ListNode(val)
                res_list = res_list.next
            lists[id] = lists[id].next
            if(lists[id] != None):
                my_heap.put((lists[id].val, id))

        return first_node
