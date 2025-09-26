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
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # maintain an unchanging reference to node ahead of the return node.
        new = ListNode(-1)
        curr = new
        print(f'  Run:0')
        print('--------------------------------------curr = new ')
        print_list('[0] curr',curr)
        print_list('[0] new ',new)
        print_address('[0] curr',curr)
        print_address('[0] new ',new)
        run = 1
        while l1 and l2:
            print(f'\n\n  Run:{run}')
            print_list('[1] l1   ',l1)
            print_list('[1] l2   ',l2)
            print_address('[1] l1   ',l1)
            print_address('[1] l2   ',l2)
            print(' -------------------------------------- compare l1.val and l2.val')
            if l1.val <= l2.val:
                print(' --------------------------------------😾curr.next = l1 因為 l1.head 是最小值, 所以把他給 curr.next, 且 new 同步改變 ')
                curr.next = l1
                l1 = l1.next
            else:
                print(' --------------------------------------😾curr.next = l2 因為 l2.head 是最小值, 所以把他給 curr.next, 且 new 同步改變 ')
                curr.next = l2
                l2 = l2.next
            print_list('[2] curr',curr)
            print_list('[2] new ',new)
            print_address('[2] curr',curr)
            print_address('[2] new ',new)
            print(' --------------------------------------curr = curr.next 因為 curr.head 是最小值已經給 new, 所以 curr 往下走一個 ')
            curr = curr.next
            print_list('[3] curr',curr)
            print_list('[3] new ',new)
            print_address('[3] curr',curr)
            print_address('[3] new ',new)
            run = run + 1
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        print('\n\nbreak while')
        print(' -------------------------------------- check l1 and l2')
        if l1 is not None:
            print(' --------------------------------------😾curr.next = l1')
            curr.next = l1
        else: 
            print(' --------------------------------------😾curr.next = l2')
            curr.next = l2
        print_list('[4] curr',curr)
        print_list('[4] new ',new)
        print_address('[4] curr',curr)
        print_address('[4] new ',new)
        return new.next

# ======= 工具函式 =======
def list_to_linked(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
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
        values.append(str(hex(id(node)))[5:11])
        # values.append(str(hex(id(node))))
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
# print('\n ---------- 初始化 p2 = p1, 他們指向相同的地址（ p1/p2 他們本身還有自己的 address ）')
# p2 = p1
# print_address('p2',p2)
# print_address('p1',p1)

# print('\n ---------- 當 p2 = l1, p2 變成了 l1, 連帶 l1 所有的 node')
# print_address('l1',l1)
# p2 = l1
# print_address('p2',p2)
# print_address('p1',p1)

# p3 = ListNode(-1)
# print('\n ---------- 初始化 p4 = p3, 他們指向相同的地址 ')
# p4 = p3
# print_address('p3',p3)
# print_address('p4',p4)
# print('\n ---------- 當 p4.next = l1, 因 p4 p3 有相同的地址，所以 p3 的 next 同步改變 ')
# print_address('l1',l1)
# p4.next = l1
# print_address('p4',p4)
# print_address('p3',p3)

