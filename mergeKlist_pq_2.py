import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 定義小於運算，讓 ListNode 可以比較
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # 初始化，把每個 list 的第一個節點丟進 heap
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        dummy = ListNode(0)
        current = dummy

        while heap:
            node = heapq.heappop(heap)   # 直接得到最小的節點
            current.next = node
            current = current.next

            if node.next:                # 下一個節點也放進 heap
                heapq.heappush(heap, node.next)

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