class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root_val

    def peek(self):
        return self.heap[0] if self.heap else None

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == idx:
                break

            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest


h = MaxHeap()
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