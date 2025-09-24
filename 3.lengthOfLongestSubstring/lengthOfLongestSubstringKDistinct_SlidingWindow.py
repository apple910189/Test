class Solution:
	def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
		n = len(s)
		max_size = 0
		counter = collections.Counter()
		
		left = 0
		for right in range(n):
			counter[s[right]] += 1
			
			while len(counter) > k: 
				counter[s[left]] -= 1
				if counter[s[left]] == 0:
					del counter[s[left]]
				left += 1
			
			max_size = max(max_size, right - left + 1)
					
		return max_size


'''
好 👌 這個版本是用 **雙指標滑動視窗 (two pointers + sliding window)** 來解 `Longest Substring with At Most K Distinct Characters`，比起你剛剛的 **二分搜尋版本**更直觀。

我幫你畫成 **流程圖 + 視覺化範例**。

---

## 1. 程式邏輯流程圖

```
輸入 s, k
	 │
	 ▼
初始化：
n = len(s)
max_size = 0
counter = {}
left = 0
	 │
	 ▼
for right in [0..n-1]:   ← 遍歷字串
	counter[s[right]] += 1
	│
	├─ while len(counter) > k:   ← 超過 k 種字元就縮小左邊
	│        counter[s[left]] -= 1
	│        如果 = 0 → 刪掉該字元
	│        left += 1
	│
	└─ 更新 max_size = max(max_size, right - left + 1)
	 │
	 ▼
回傳 max_size
```

---

## 2. 視覺化範例

假設：

```
s = "eceba", k = 2
```

---

### Step 1

* left = 0, right = 0, counter = {e:1}
* distinct = 1 ≤ k
* max\_size = max(0, 0-0+1) = 1
  視窗 = `[e]`

---

### Step 2

* right = 1 → 加入 `"c"`
* counter = {e:1, c:1}
* distinct = 2 ≤ k
* max\_size = max(1, 1-0+1) = 2
  視窗 = `[e c]`

---

### Step 3

* right = 2 → 加入 `"e"`
* counter = {e:2, c:1}
* distinct = 2 ≤ k
* max\_size = max(2, 2-0+1) = 3
  視窗 = `[e c e]` ✅ 最長

---

### Step 4

* right = 3 → 加入 `"b"`
* counter = {e:2, c:1, b:1}
* distinct = 3 > k → 需要縮左邊

縮左：left=0 → 移出 `"e"`
counter = {e:1, c:1, b:1} (還是 3 個)
left=1 → 移出 `"c"`
counter = {e:1, b:1} (2 個) ✅

現在 left=2, 視窗 = `[e b]`
max\_size = max(3, 3-2+1) = 3

---

### Step 5

* right = 4 → 加入 `"a"`
* counter = {e:1, b:1, a:1} (3 個 > k)
  縮左：

  * 移出 `"e"` → {b:1, a:1}
  * left=3
	視窗 = `[b a]`
	max\_size = max(3, 4-3+1) = 3

---

✅ 最終答案 = 3
對應子字串 `"ece"` 或 `"ceb"`。

---

## 3. 重點圖解

```
右指標 right → 不斷往右擴展
左指標 left → 在超過 k 種字元時往右收縮
max_size → 紀錄目前最大合法視窗
```

---

要不要我幫你畫成 **一條字串上動態移動 \[left, right] 視窗的圖**（像動畫時間線那樣），讓你直覺看到 `eceba` 的視窗如何移動？

'''