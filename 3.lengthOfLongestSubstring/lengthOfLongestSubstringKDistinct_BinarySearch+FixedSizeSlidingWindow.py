class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n:
            return n
        left, right = k, n
        
        def isValid(size):
            counter = collections.Counter(s[:size])
            if len(counter) <= k:
                return True
            for i in range(size, n):
                counter[s[i]] += 1
                counter[s[i - size]] -= 1
                if counter[s[i - size]] == 0:
                    del counter[s[i - size]]
                if len(counter) <= k:
                    return True
            return False
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if isValid(mid):
                left = mid
            else:
                right = mid - 1
        
        return left


'''
好 👍 這段程式是 **Longest Substring with At Most K Distinct Characters** 的 **二分搜尋 + 滑動視窗檢查** 解法。
我幫你拆解成 **流程圖 + 視覺範例**。

---

## 1. 程式邏輯流程圖

```
輸入 s, k
     │
     ▼
n = len(s)
如果 k >= n → 回傳 n
     │
     ▼
left = k, right = n
     │
     ▼
while left < right:
    mid = (left + right + 1) // 2   ← 二分搜尋長度
    │
    ├─ isValid(mid) ?
    │       │
    │       ├─ True → left = mid
    │       └─ False → right = mid - 1
     │
     ▼
回傳 left
```

---

## 2. `isValid(size)` 檢查子字串長度是否合法

流程：

```
輸入 size
     │
     ▼
建立 counter = s[0:size] 的字元計數
     │
     ├─ 如果 distinct 字元數 <= k → True
     │
     ▼
for i in range(size, n):  ← 滑動視窗
    counter[s[i]] += 1
    counter[s[i - size]] -= 1
    如果 counter[s[i - size]] == 0:
        刪除該字元
    │
    ├─ 如果 distinct 字元數 <= k → True
     │
     ▼
全部檢查完 → False
```

---

## 3. 視覺化範例

假設：

```
s = "eceba", k = 2
```

### Step 1: 初始化

* n = 5
* k = 2
* left = 2, right = 5

---

### Step 2: Binary Search

#### 迴圈 1

* mid = (2 + 5 + 1) // 2 = 4
* 檢查長度 4 是否有合法子字串

檢查 `"eceb"`

* counter = {e:2, c:1, b:1} → 3 種字元 > k (失敗)
  移動視窗 → `"ceba"`
* counter = {c:1, e:1, b:1, a:1} → 4 種字元 > k (失敗)
  → isValid(4) = False

更新 → right = 3

---

#### 迴圈 2

* mid = (2 + 3 + 1) // 2 = 3
* 檢查長度 3 是否有合法子字串

檢查 `"ece"`

* counter = {e:2, c:1} → 2 種字元 ≤ k ✅
  → isValid(3) = True

更新 → left = 3

---

現在 left = 3, right = 3 → while 結束

---

### Step 3: 回傳答案

最後答案 = 3
對應的子字串 `"ece"`。

---

## 4. 重點圖解

二分搜尋 → 找最長長度
每次用 `isValid(mid)` 滑動視窗檢查
✅ 合法就往大找
❌ 不合法就往小找

---

要不要我幫你畫成 **二分搜尋範例動畫圖**（left, right, mid 移動過程 + 視窗檢查示意圖）？

'''