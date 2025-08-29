from typing import List, Optional

# part 2 python code
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node
        
    def __lt__(self, other):
      return self.value < other.value

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        if not lists:
            return None
        
        for node in lists:
            if node:
                heappush(pq, node)
        
        head = None
        now_node = None
        
        while len(pq) > 1:
            node = heappop(pq)
            if not head:
                head = node
                now_node = node
            else:
                now_node.set_next(node)
                now_node = now_node.get_next()
            
            node = node.get_next()
            if node:
                heappush(pq, node)
        if head == None:
            if len(pq) != 0:
                head = pq[0];
        else:
            now_node.setNext(heappop(pq))
        return head

