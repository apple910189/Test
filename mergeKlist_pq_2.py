import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 定義小於運算，讓 ListNode 可以比較
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # 初始化，把每個 list 的第一個節點丟進 heap
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        dummy = ListNode(0)
        current = dummy

        while heap:
            node = heapq.heappop(heap)   # 直接得到最小的節點
            current.next = node
            current = current.next

            if node.next:                # 下一個節點也放進 heap
                heapq.heappush(heap, node.next)

        return dummy.next


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
        result.append(node.val)
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

print(linkedlist_to_list(merged))  # 預期輸出: [1,1,2,3,4,4,5,6]





'''
好問題 👍
我用圖解來幫你理解這個演算法的流程。這個方法用 **最小堆 (min heap)** 來做多個已排序 linked list 的合併。

我們假設有四個排序好的 linked list：

```
list1: 1 → 4 → 7
list2: 2 → 5 → 8
list3: 3 → 6 → 9
list4: 0 → 10
```

---

### Step 1. 初始化 heap

把四個 list 的第一個節點丟進 heap：

```
heap = [1, 2, 3, 0]
```

(實際上是 ListNode，但用值表示)

因為 heap 會自動保持最小堆，所以結構會像這樣：

```
        0
       / \
      1   3
     /
    2
```

---

### Step 2. 建立 dummy

```
dummy → None
current → dummy
```

---

### Step 3. 從 heap pop 最小值

取出最小的 `0`：

```
heap = [1, 2, 3]
```

接到結果串列：

```
dummy → 0
current → 0
```

把 `0` 的下一個節點 `10` 放進 heap：

```
heap = [1, 2, 3, 10]
```

---

### Step 4. 重複流程

* 取出最小 `1`
  結果： `0 → 1`
  heap 放入 `4` → `[2, 4, 3, 10]`

* 取出最小 `2`
  結果： `0 → 1 → 2`
  heap 放入 `5` → `[3, 4, 10, 5]`

* 取出最小 `3`
  結果： `0 → 1 → 2 → 3`
  heap 放入 `6` → `[4, 5, 10, 6]`

* 取出最小 `4`
  結果： `0 → 1 → 2 → 3 → 4`
  heap 放入 `7` → `[5, 6, 10, 7]`

---

### Step N. 繼續直到 heap 空

最後結果會是：

```
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10
```

---

📊 **流程圖概念**

```
lists = [list1, list2, list3, list4]

         ┌─────────────────────────┐
         │   初始化：push 每個頭節點   │
         └────────────┬────────────┘
                      ↓
                 ┌─────────┐
                 │ heap 不空 │───No───> 結束
                 └────┬────┘
                      │Yes
                      ↓
              pop 最小節點 (node)
                      │
                      ↓
        current.next = node, 移動 current
                      │
                      ↓
        如果 node.next 存在 → push 進 heap
                      │
                      ↓
                  回到檢查
```

---

要不要我幫你畫成 **一步步的圖示 (箭頭串起來的 list + heap 狀態)**，像動畫那樣？這樣你就能直觀看到 heap 和結果串列是怎麼演變的。

'''
