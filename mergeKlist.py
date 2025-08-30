# part 2 python code
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    def getNext(self):
        return self.next
    
    def setNext(self, next_node):
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
        
        while pq:
            node = heappop(pq)
            
            if not head:
                head = node
                now_node = node
            else:
                now_node.setNext(node)
                now_node = now_node.getNext()
            
            if node.getNext():
                heappush(pq, node.getNext())
        
        return head