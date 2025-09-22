import utils as u


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(' #1 創建 values list')
        values = []
        for l in lists:
            print(' #2 把 lists 中的每一個 node 的所有 node.val 都加到 values')
            while l:
                print(f' #3 加入node val: {l.val}')
                values.append(l.val)
                print(f' #4 node 往下走')
                l = l.next
        print(' #5 排序 values ')
        print(' #6 創建 head 與 point, 初始值為 0')
        head = point = ListNode(0)
        print(' #7 利用 point 與排序好的 values list 中的值, 來建立 head 的所有 node')
        for x in sorted(values):
            point.next = ListNode(x)
            point = point.next

        return head.next

'''

'''

# ===== 輔助方法 =====
def list_to_linkedlist(arr):
    """把普通 list 轉換成 LinkedList"""
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    """把 LinkedList 轉換回 list"""
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