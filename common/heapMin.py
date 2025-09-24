class MinHeap:
	def __init__(self):
		self.heap = []

	def push(self, val):
		"""插入元素"""
		self.heap.append(val)
		self._sift_up(len(self.heap) - 1)

	def pop(self):
		"""取出最小值"""
		if not self.heap:
			return None
		if len(self.heap) == 1:
			return self.heap.pop()

		root_val = self.heap[0]
		# 把最後一個元素放到 root
		self.heap[0] = self.heap.pop()
		self._sift_down(0)
		return root_val

	def peek(self):
		"""查看最小值（不刪除）"""
		return self.heap[0] if self.heap else None

	def _sift_up(self, idx):
		"""往上調整"""
		parent = (idx - 1) // 2             # 找到父節點位置
		while idx > 0 and self.heap[idx] < self.heap[parent]:
			self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]   # 換位置
			idx = parent                    # 繼續往上
			parent = (idx - 1) // 2

	def _sift_down(self, idx):
		"""往下調整"""
		n = len(self.heap)
		while True:
			smallest = idx                  # 假設自己是最小
			left = 2 * idx + 1
			right = 2 * idx + 2

			if left < n and self.heap[left] < self.heap[smallest]:
				smallest = left
			if right < n and self.heap[right] < self.heap[smallest]:
				smallest = right

			if smallest == idx:             # 如果自己最小，停止
				break

			self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
			idx = smallest                  # 繼續往下



h = MinHeap()
h.push(5)
h.push(3)
h.push(8)
h.push(1)
h.push(2)

print("Heap:", h.heap)   # 內部結構 (可能是 [1,2,8,5,3]，符合 min-heap 規則)

print(h.pop())  # 1
print(h.pop())  # 2
print(h.pop())  # 3
print(h.pop())  # 5
print(h.pop())  # 8