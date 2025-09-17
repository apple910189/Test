
'''
在 Python 中，物件之間如果要比較大小 (<, >, <=, >=)，就必須定義「魔術方法 (Magic Method)」。

__lt__ 代表 "less than" (<)
__gt__ 代表 "greater than" (>)
__eq__ 代表 "equal" (==)
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
                heapq.heappush(heap, (node.val, i, node)) # 在 Python 裡，tuple 預設可以比較（會逐一比對元素）

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