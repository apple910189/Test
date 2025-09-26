'''
問題：current 本身是什麼？
指標是什麼？
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_node(nodeName, node):
    # print_val(nodeName,node)
    # print_address(nodeName,node)
    print_valAndAddress(nodeName,node)

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

def print_step(string):
    print(f' ---------------- {string}')

dummy = ListNode(0)
current = dummy
print_step('創建 dummy 與 current')
print_node('current',current)
print_node('dummy  ',dummy)

print_step('修改 currnet.val 會同時修改 dummy.val')
current.val = 1
print_node('current',current)
print_node('dummy  ',dummy)

print_step('修改 current.next 會同時修改 dummy.next')
current.next = ListNode(2)
print_node('current',current)
print_node('dummy  ',dummy)

print_step('修改 current 不會同時修改 dummy')
current = current.next
print_node('current',current)
print_node('dummy  ',dummy)

print_step('修改 currnet.val 會同時修改 dummy.val')
current.val = 3
print_node('current',current)
print_node('dummy  ',dummy)









