
def print_val(listName, node):
    """把鏈結串列轉回字串輸出"""
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(f'{listName}: {" -> ".join(vals)}')

def print_address(nodeName, node):
    vals = []
    while node:
        vals.append(str(hex(id(node)))[5:11])
        node = node.next
    print(f'{nodeName}: {" -> ".join(vals)}')

def print_valAndAddress(nodeName, node):
    nodeAddress = []
    nodevals = []
    while node:
        nodeAddress.append(str(hex(id(node)))[5:11])
        nodevals.append(str(node.val))
        node = node.next
    newList = []
    for i in range(len(nodeAddress)):
        str1 = f'({nodevals[i]}) {nodeAddress[i]}'
        newList.append(str1)
    print(f'{nodeName}: {" -> ".join(newList)}')

def print_node(nodeName, node):
    # print_val(nodeName,node)
    # print_address(nodeName,node)
    print_valAndAddress(nodeName,node)

def print_run(run):
    print(f'\n    while 迴圈 {run}')

def print_step(string):
    print(f' ---------------- {string}')

# ======= 測試 =======
# class ListNode:
#     def __init__( val=0, next=None):
#         self.val = val
#         self.next = next
    
#     def get_next(self):
#         return self.next
    
#     def set_next( next_node):
#         self.next = next_node

#     def go_next(self):
#         self = self.next;

# def list_to_linked(lst):
#     """把 Python list 轉換成鏈結串列"""
#     if not lst:
#         return None
#     head = ListNode(lst[0])
#     current = head
#     for val in lst[1:]:
#         node = ListNode(val)
#         current.set_next(node)
#         current = node
#     return head



# l1 = [2,4]
# l2 = [1,3,5]
# l3 = [9]
# u = Utils()
# list1 = list_to_linked(l1)
# list2 = list_to_linked(l2)
# list3 = list_to_linked(l3)
# u.print_node('list1',list1)


