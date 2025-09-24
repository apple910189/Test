from collections import Counter


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		chars = Counter()

		left = right = 0

		res = 0
		while right < len(s):
			r = s[right]
			chars[r] += 1

			while chars[r] > 1:
				l = s[left]
				chars[l] -= 1
				left += 1

			res = max(res, right - left + 1)

			right += 1
		return res

sol = Solution()
res = sol.lengthOfLongestSubstring('aab')
print(res)

'''
好 👍 這一版程式碼是 **滑動視窗 (sliding window)** 的解法，比剛才的暴力法更快 (O(n))。
我用圖解來幫你說明 **`left` 和 `right` 怎麼移動**，以及 `chars` (Counter) 如何記錄目前視窗內的字元。

---

### 範例：

`s = "abcabcbb"`

---

### 初始狀態

```
left = 0, right = 0, res = 0
chars = {}
```

---

### Step 1: right = 0

視窗 = `"a"`

```
chars = { 'a': 1 }
res = max(0, 0 - 0 + 1) = 1
```

```
[a] b c a b c b b
 ↑
left=0
```

---

### Step 2: right = 1

視窗 = `"ab"`

```
chars = { 'a': 1, 'b': 1 }
res = max(1, 1 - 0 + 1) = 2
```

```
[a b] c a b c b b
 ↑
left=0
```

---

### Step 3: right = 2

視窗 = `"abc"`

```
chars = { 'a': 1, 'b': 1, 'c': 1 }
res = max(2, 2 - 0 + 1) = 3
```

```
[a b c] a b c b b
 ↑
left=0
```

---

### Step 4: right = 3

視窗 = `"abca"` → 'a' 重複

```
chars = { 'a': 2, 'b': 1, 'c': 1 }
```

進入 while 迴圈縮小左邊：

* 移除 `s[left]='a'` → left = 1
* chars = { 'a': 1, 'b': 1, 'c': 1 }

視窗 = `"bca"`

```
res = max(3, 3 - 1 + 1) = 3
```

```
a [b c a] b c b b
   ↑
 left=1
```

---

### Step 5: right = 4

視窗 = `"bcab"` → 'b' 重複

```
chars = { 'a': 1, 'b': 2, 'c': 1 }
```

while 收縮左邊：

* 移除 `s[1]='b'` → left=2 → chars = { 'a':1, 'b':1, 'c':1 }

視窗 = `"cab"`

```
res = max(3, 4 - 2 + 1) = 3
```

```
a b [c a b] c b b
	 ↑
	left=2
```

---

### Step 6: right = 5

視窗 = `"cabc"` → 'c' 重複

```
chars = { 'a':1, 'b':1, 'c':2 }
```

while 收縮左邊：

* 移除 `s[2]='c'` → left=3 → chars = { 'a':1, 'b':1, 'c':1 }

視窗 = `"abc"`

```
res = max(3, 5 - 3 + 1) = 3
```

```
a b c [a b c] b b
	   ↑
	  left=3
```

---

### Step 7: right = 6

視窗 = `"abcb"` → 'b' 重複

```
chars = { 'a':1, 'b':2, 'c':1 }
```

while 收縮左邊：

* 移除 `s[3]='a'` → left=4 → chars = { 'a':0, 'b':2, 'c':1 }
* 移除 `s[4]='b'` → left=5 → chars = { 'a':0, 'b':1, 'c':1 }

視窗 = `"cb"`

```
res = max(3, 6 - 5 + 1) = 3
```

```
a b c a b [c b] b
		 ↑
		left=5
```

---

### Step 8: right = 7

視窗 = `"cbb"` → 'b' 重複

```
chars = { 'c':1, 'b':2 }
```

while 收縮左邊：

* 移除 `s[5]='c'` → left=6 → chars = { 'c':0, 'b':2 }
* 移除 `s[6]='b'` → left=7 → chars = { 'c':0, 'b':1 }

視窗 = `"b"`

```
res = max(3, 7 - 7 + 1) = 3
```

```
a b c a b c b [b]
		   ↑
		  left=7
```

---

### 最終結果

最大長度 = **3**
最長子字串有 `"abc"`, `"bca"`, `"cab"`。

---

要不要我幫你畫成 **一個格子動畫圖**，左指標 (`left`) 和右指標 (`right`) 移動起來，就像窗戶一樣？

'''