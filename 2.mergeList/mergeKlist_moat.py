# part 2 python code
import heapq
from typing import List, Optional
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
				heapq.heappush(pq, node)
		
		head = None
		now_node = None
		
		while pq:
			node = heapq.heappop(pq)
			
			if not head:
				head = node
				now_node = node
			else:
				now_node.setNext(node)
				now_node = now_node.getNext()
			
			if node.getNext():
				heapq.heappush(pq, node.getNext())
		
		return head

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
		result.append(node.value)
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

print(f'結果：{linkedlist_to_list(merged)}')  # 預期輸出: [1,1,2,3,4,4,5,6]
'''
你這段程式碼 👍 完全正確地實作了 **k 個已排序 linked list 的合併**，而且跟之前版本一樣使用了 `heapq` (最小堆)，只是這裡加了 getter / setter 方法來操作 `next`。

我幫你拆解一下：

---

### 🔑 程式邏輯解說

1. **ListNode 定義**

   ```python
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
   ```

   * `__lt__` (`<`) 運算子 overloading 讓 `heapq` 可以比較 `ListNode`，根據 `value` 排序。
   * `getNext` / `setNext` 是封裝操作，功能上和 `self.next` 一樣，只是更物件導向。

---

2. **初始化 heap**

   ```python
   pq = []
   for node in lists:
	   if node:
		   heappush(pq, node)
   ```

   * 把每個 linked list 的第一個節點放進最小堆。
   * 堆內會根據節點值自動排序。

---

3. **建立結果串列**

   ```python
   head = None
   now_node = None
   ```

   * `head` 用來記錄最終結果的開頭。
   * `now_node` 用來追蹤目前插到哪裡。

---

4. **逐步合併**

   ```python
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
   ```

   * 從堆中取出最小節點。
   * 如果結果 list 還沒開始，初始化 `head`。
   * 否則，把 `node` 接到 `now_node` 後面。
   * 如果 `node` 還有下一個節點，就把它放進堆，等待後面處理。

---

5. **回傳**

   ```python
   return head
   ```

   * 最後得到的就是完整的合併後串列。

---

### ✅ 與之前版本差異

* 你這版沒有用 dummy node，而是用 `head = None` 來處理第一次連接的情況。
* 功能一樣，只是少了一個額外的 dummy 節點。
* dummy 節點的優點是可以避免「第一次判斷 head 是否為空」這一步，但你的方式同樣正確。

---

要不要我幫你畫成一個「流程圖 + heap 變化圖」對應這段 **getter/setter 版本**的程式？

'''