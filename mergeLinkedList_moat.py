# mergeLinkedList (moat)

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        nowNode = None
        list1Pointer = list1
        list2Pointer = list2
        if list1 is None and list2 is None: 
            print_step('Warning: Both two lists are None')
            return head 
        if list1 is None:
            print_step('Warning: list1 is None')
            return list2
        if list2 is None:
            print_step('Warning: list2 is None')
            return list1
        
        if list1.value <= list2.value:
            head = list1Pointer
            list1Pointer = list1Pointer.get_next()
        else:
            head = list2Pointer
            list2Pointer = list2Pointer.get_next()
        nowNode = head
        run = 1
        while list1Pointer is not None and list2Pointer is not None:
            if list1Pointer.value <= list2Pointer.value:
                nowNode.set_next(list1Pointer)
                list1Pointer = list1Pointer.get_next()
            else:
                nowNode.set_next(list2Pointer)
                list2Pointer = list2Pointer.get_next()
            nowNode = nowNode.get_next()
            run = run + 1
        if list1Pointer is not None: 
            nowNode.set_next(list1Pointer)
        else: # 如果 l2 有剩下
            nowNode.set_next(list2Pointer)
        return head # 返回 head


# ======= 工具函式 =======
def list_to_linked(lst):
    """把 Python list 轉換成鏈結串列"""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        node = ListNode(val)
        current.set_next(node)
        current = node
    return head

def print_list(listName, node: Optional[ListNode]):
    """把鏈結串列轉回字串輸出"""
    values = []
    while node:
        values.append(str(node.value))
        node = node.get_next()
    print(f'{listName}: {" -> ".join(values)}')

def print_address(nodeName, node: Optional[ListNode]):
    values = []
    while node:
        values.append(str(hex(id(node)))[5:11])
        node = node.next
    print(f'{nodeName}: {" -> ".join(values)}')

def print_listAndAddress(nodeName, node: Optional[ListNode]):
    nodeAddress = []
    nodeValues = []
    while node:
        nodeAddress.append(str(hex(id(node)))[5:11])
        nodeValues.append(str(node.value))
        node = node.next
    newList = []
    for i in range(len(nodeAddress)):
        str1 = f'({nodeValues[i]}) {nodeAddress[i]}'
        newList.append(str1)
    print(f'{nodeName}: {" -> ".join(newList)}')

def print_node(nodeName, node: Optional[ListNode]):
    print_list(nodeName,node)
    # print_address(nodeName,node)
    # print_listAndAddress(nodeName,node)

def print_run(run):
    print(f'\n    while 迴圈 {run}')

def print_step(string):
    print(f' ---------------- {string}')

# ======= 測試 =======

l1 = [2,4]
l2 = [1,3,5]
l3 = [9]

list1 = list_to_linked(l1)
list2 = list_to_linked(l2)
list3 = list_to_linked(l3)

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)
print_node('merged',merged)


# list1P = list1
# list2P = list2
# print_node('list1 ',list1)
# print_node('list1P',list1P)
# print(' -------------------------------------- list1P.set_next(l3)')
# list1P.set_next(list3)
# print_node('list1P',list1P)
# print_node('list1 ',list1)


# n1 = ListNode(1)
# n3 = ListNode(1)
# n2 = n1
# print_node('n1',n1)
# print_node('n2',n2)

# n1 = list1
# # n1.next = list2

# print_node('n1',n1)
# print_node('n2',n2)









