
'''
Approach 3: Optimize Approach 2 by Priority Queue
Algorithm

Almost the same as the one above but optimize the comparison process by priority queue. You can refer here for more information about it.

Complexity Analysis

Time complexity : O(Nlogk) where k is the number of linked lists.

The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
There are N nodes in the final linked list.
Space complexity :

O(n) Creating a new linked list costs O(n) space.
O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).
'''
import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # 初始化，把每個 list 的第一個節點放進 heap
        for i, node in enumerate(lists):
            if node:
                # (值, index, node) -> index 保證在值相同時不會比較 node 物件
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ===== 輔助方法 =====
def list_to_linkedlist(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ===== 測試 =====
lists = [
    list_to_linkedlist([1,4,5]),
    list_to_linkedlist([1,3,4]),
    list_to_linkedlist([2,6])
]

solution = Solution()
merged = solution.mergeKLists(lists)

print(linkedlist_to_list(merged))  # 預期輸出: [1,1,2,3,4,4,5,6]