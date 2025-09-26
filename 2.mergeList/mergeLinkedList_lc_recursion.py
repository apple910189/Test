# mergeLinkedList (leetcode)

from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        print('--- start ---')
        if not list1 or not list2:
            print_list('return list1',list1) if list1 else print_list('return list2',list2)
            return list1 if list1 else list2
        print_list('list1',list1)
        print_list('list2',list2)
        if list1.val > list2.val:
            list1, list2 = list2, list1
            print_list('list1sw',list1)
            print_list('list2sw',list2)

        list1.next = self.mergeTwoLists(list1.next, list2)
        print_list('return list1',list1)
        return list1
    '''
    l1: [1,2]
    l2: [3,4]
    m(1,3)
      |
    m(2,3)
       \
    m(n,3)

    l1: [1,3,5]
    l2: [2,4,6]
    m(1,2)
      \
       --------\
    m(3,2) >> m(2,3)
                |
    m(4,3) >> m(3,4)
                |
    m(5,4) >> m(4,5)
                |
    m(6,5) >> m(5,6)
        -	 --/
            /
    m(none,6)
    '''

# ======= 工具函式 =======
def list_to_linked(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    print(lst[1:])
    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(listName, node: Optional[ListNode]):
    """把鏈結串列轉回字串輸出"""
    values = []
    while node:
        values.append(str(node.val))
        node = node.get_next()
    print(f'{listName}: {" -> ".join(values)}')

def print_address(nodeName, node: Optional[ListNode]):
    values = []
    while node:
        values.append(str(hex(id(node)))[5:10])
        node = node.next
    print(f'{nodeName}: {" -> ".join(values)}')


# ======= 測試 =======
list1 = [1,3,5]
list2 = [2,4,6]
list3 = [5,6]

l1 = list_to_linked(list1)
l2 = list_to_linked(list2)
l3 = list_to_linked(list3)

sol = Solution()
merged = sol.mergeTwoLists(l1, l2)
print_list('合併後結果：',merged)


# print('關於 linked list address 注意事項')
# p1 = ListNode(-1)
# print('\n ---------- 初始化 p2 = p1, 他們有相同的 head  ')
# p2 = p1
# print_address('p2',p2)
# print_address('p1',p1)
# print('\n ---------- 當 p2 = l1, 只有 p2 的 head 被改變')
# print_address('l1',l1)
# p2 = l1
# print_address('p2',p2)
# print_address('p1',p1)

# p3 = ListNode(-1)
# print('\n ---------- 初始化 p4 = p3, 他們有相同的 head ')
# p4 = p3
# print_address('p3',p3)
# print_address('p4',p4)
# print('\n ---------- 當 p4.next = l1, 因 p4/p3 有相同的 head ，所以他們的 next 同步改變 ')
# print_address('l1',l1)
# p4.next = l1
# print_address('p4',p4)
# print_address('p3',p3)






