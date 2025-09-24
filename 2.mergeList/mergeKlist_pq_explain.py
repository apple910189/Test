'''
好 👍 你問得很對，heapq 是 Python 處理 最小堆 (min-heap) 的內建模組，在這題 mergeKLists 特別好用。
我來慢慢說明：

1. 什麼是 Heap？
	•    Heap (堆積) 是一種樹狀結構，最常用的是 最小堆 (min-heap)。
	•    在 最小堆 中：
	•    父節點一定 ≤ 子節點
	•    也就是說，堆頂 (root) 永遠是目前最小的元素。

這樣就能很快找到最小值，並在 log 時間內插入 / 刪除。

2. Python 的 heapq
	•    Python 的 heapq 用 list 來模擬 min-heap。
	•    常用函式：
'''

import heapq

heap = []
heapq.heappush(heap, 3)   # 加入 3
heapq.heappush(heap, 1)   # 加入 1
heapq.heappush(heap, 5)   # 加入 5
print(heap)  # [1, 3, 5] (內部結構保持 heap 特性)

smallest = heapq.heappop(heap)  # 拿出最小值 (1)
print(smallest)  # 1
print(heap)  # [3, 5]


'''
👉 heapq 其實是用 list 表示，但會自動維護「最小值在最前面」。

3. 在 mergeKLists 裡怎麼用？
	•    我們有 k 條 linked list，要一直取 目前所有 list 的最小節點。
	•    用 heapq 的流程是：
	1.    先把每條 list 的 第一個節點 丟進 heap。
	2.    每次從 heap 拿出最小值（O(log k)）。
	3.    如果那個節點有 next，把 next 再丟進 heap。
	4.    重複直到 heap 空。

這樣，每次只處理一個節點，不需要先把所有值收集再排序。

4. 為什麼要 (val, i, node)？

在程式裡我們用：

heapq.heappush(heap, (node.val, i, node))

原因是：
	•    heapq 會比較 tuple 的第一個值 (node.val)。
	•    如果有相同的 val，就會比較第二個值 (i)。
	•    如果只放 (node.val, node)，當 val 相同時，Python 會嘗試比較 node（ListNode 物件），但 ListNode 沒有定義比較方法，就會出錯。

👉 所以我們加 i（list 的索引），確保比較不會出錯。

5. 複雜度
	•    假設總共有 N 個節點，k 條 list。
	•    每次 heappush / heappop 都是 O(log k)。
	•    總共要做 N 次操作。

➡️ 總時間複雜度 = O(N log k)
比收集所有值再排序的 O(N log N) 高效，尤其當 k << N 時。

要不要我幫你畫一個小例子，用三條 list [1,4,5]、[1,3,4]、[2,6]，示範 heap 裡的變化？

'''