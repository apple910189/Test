class Solution:
	def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
		max_size = 0
		counter = collections.Counter()
		
		for right in range(len(s)):
			counter[s[right]] += 1
			
			if len(counter) <= k:
				max_size += 1
			else:
				counter[s[right - max_size]] -= 1
				if counter[s[right - max_size]] == 0:
					del counter[s[right - max_size]]

		return max_size

'''
好，我來幫你畫圖解釋這一版程式 👇

這個版本是 **不同於經典滑動視窗的寫法**：

* 經典解法會用 `left` 來代表左邊界，不斷調整。
* 這裡沒有 `left`，而是靠 **`max_size` (目前已知的最長合法長度)** 來「間接計算左邊界」。

---

## 1. 程式邏輯流程圖

```
輸入 s, k
	 │
	 ▼
max_size = 0
counter = {}
	 │
	 ▼
for right in range(len(s)):
	counter[s[right]] += 1
	│
	├─ 如果 distinct 字元數 ≤ k:
	│        max_size += 1    ← 視窗往右擴大
	│
	└─ 否則 (distinct > k):
			 移除左邊界字元 s[right - max_size]
			 如果該字元數量=0 → 刪掉
			 （視窗縮小一格）
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

* right = 0, 加入 `'e'`
* counter = {e:1}
* distinct = 1 ≤ 2 → max\_size = 1
* 視窗 = `[e]`

---

### Step 2

* right = 1, 加入 `'c'`
* counter = {e:1, c:1}
* distinct = 2 ≤ 2 → max\_size = 2
* 視窗 = `[e c]`

---

### Step 3

* right = 2, 加入 `'e'`
* counter = {e:2, c:1}
* distinct = 2 ≤ 2 → max\_size = 3
* 視窗 = `[e c e]` ✅

---

### Step 4

* right = 3, 加入 `'b'`
* counter = {e:2, c:1, b:1}
* distinct = 3 > 2 → 不合法
  👉 移除 **最左邊元素** `s[3 - 3] = s[0] = 'e'`
* counter = {e:1, c:1, b:1}
* distinct = 3 (還是不合法)，但程式只刪一次，所以會卡住在 3 種字元。
* max\_size = 3（沒有更新）
* 視窗（理想狀態應該變成 `[c e b]`，但實際上這個寫法不是很正確）

---

### Step 5

* right = 4, 加入 `'a'`
* counter = {e:1, c:1, b:1, a:1}
* distinct = 4 > 2
  👉 移除 `s[4 - 3] = s[1] = 'c'`
* counter = {e:1, c:0, b:1, a:1} → {e:1, b:1, a:1}
* distinct = 3（仍大於 2）
* max\_size = 3

---

## 3. 最終輸出

回傳 `max_size = 3`
對應最長合法子字串 `"ece"`。

---

## 4. 重點圖解

* **`max_size` 同時表示目前的視窗長度**。
* 每次加入新字元 → 如果沒超過 k，就擴張。
* 如果超過 k → 移除 **視窗左端 (right - max\_size)** 的字元，視窗維持長度不變。

---

⚠️ 不過這個版本的寫法其實 **有一點不嚴謹**：

* 在超過 k 種字元時，它只會刪 **一次左邊元素**，但如果還是不合法，就不再繼續刪。
* 所以它能跑過一些測資（像 `"eceba", k=2`），但在某些情況會出錯。

要不要我幫你舉一個「這段程式會算錯」的反例，讓你比較直觀地看到它跟正統滑動視窗的差別？


你這個觀察很棒 👏
這版程式在 **LeetCode 上是 Accepted**，的確看起來有點奇怪（因為 while 不見了只刪一次）。

---

### ✅ 為什麼它能過

關鍵在這一行：

```python
counter[s[right - max_size]] -= 1
```

它移除的不是「單純的 left」，而是 **`right - max_size`**。
這代表的意思是：「假設目前最大合法視窗長度是 `max_size`，那當我再加一個新字元 `s[right]` 之後，
如果變成不合法，那麼視窗的左邊界一定在 `s[right - max_size]` 這個位置。」

換句話說，它利用 `max_size` 來記錄 **上一個合法視窗的長度**，當下次不合法時，只要移除最舊的那個字元，就能回到合法狀態。

---

### 🔍 為什麼刪一次就夠

因為程式裡的 `max_size` 是 **「當前維持的合法最大視窗長度」**，所以：

1. 當加進一個新字元後，如果還 ≤ k → 直接擴大視窗，`max_size += 1`。
2. 如果超過 k → 就把「最左邊的舊字元」移除掉（也就是 `s[right - max_size]`）。
   這樣 counter 又會回到 ≤ k 的狀態，視窗長度依然是 `max_size`，不需要 while。

也就是說，它其實 **每次最多只會超出 1 種字元**，刪掉一次就能恢復合法。
所以 while 不是必要的。

---

### ⚠️ 缺點

這種寫法很巧妙，但不如經典滑動視窗直觀。

* 它把「左邊界」隱含在 `right - max_size`，不是顯式用 `left`。
* 可讀性差，理解成本高。
* 雖然能過測資，但維護或擴充時（例如要記錄子字串本身，而不只是長度）就會比較麻煩。

---

### ✅ 結論

這版能 Accepted 是因為：

* `max_size` 保證了「只需要刪掉一次最舊的元素就能回到合法狀態」。
* 所以 while 縮小視窗的動作，被巧妙地簡化成一次刪除。

---

要不要我幫你「畫圖」比較一下 **經典 left-right 滑動視窗** vs **這個 max\_size 寫法**，用同一個例子（比如 `"eceba", k=2`）讓你直覺看到差異？

'''