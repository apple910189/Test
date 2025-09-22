class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res


sol = Solution()
res = sol.lengthOfLongestSubstring('aab')
print(res)



'''
好的 👍 我來用圖解方式幫你理解這段程式碼在做什麼。

這段程式碼是 **Longest Substring Without Repeating Characters** 的 **暴力解法**。
它的邏輯是：

1. 用兩個指標 `i`（起點）、`j`（終點）去枚舉所有子字串。
2. 每次檢查子字串 `s[i:j]` 是否有重複字元。
3. 若沒有重複，就更新最長長度 `res`。

---

### 範例：

`s = "abcabcbb"`

---

#### 迴圈流程示意圖

**外層迴圈 i = 0**

* i = 0 → j 從 0 \~ n-1

```
j = 0: 子字串 "a" ✅ 無重複，res = 1
j = 1: 子字串 "ab" ✅ 無重複，res = 2
j = 2: 子字串 "abc" ✅ 無重複，res = 3
j = 3: 子字串 "abca" ❌ 有重複 'a'
j = 4: 子字串 "abcab" ❌ 有重複
...
```

**外層迴圈 i = 1**

* i = 1 → j 從 1 \~ n-1

```
j = 1: 子字串 "b" ✅ 無重複
j = 2: 子字串 "bc" ✅ 無重複
j = 3: 子字串 "bca" ✅ 無重複，長度 3
j = 4: 子字串 "bcab" ❌ 有重複
```

**外層迴圈 i = 2**

* i = 2 → j 從 2 \~ n-1

```
j = 2: 子字串 "c"
j = 3: 子字串 "ca"
j = 4: 子字串 "cab" ✅ 無重複，長度 3
j = 5: 子字串 "cabc" ❌ 有重複
```

---

### 視覺化表格 (✅ 表示無重複，❌ 表示有重複)

| i\j | 0  | 1   | 2    | 3     | 4      | 5       | 6        | 7         |
| --- | -- | --- | ---- | ----- | ------ | ------- | -------- | --------- |
| 0   | a✅ | ab✅ | abc✅ | abca❌ | abcab❌ | abcabc❌ | abcabcb❌ | abcabcbb❌ |
| 1   |    | b✅  | bc✅  | bca✅  | bcab❌  | bcabc❌  | bcabcb❌  | bcabcbb❌  |
| 2   |    |     | c✅   | ca✅   | cab✅   | cabc❌   | cabcb❌   | cabcbb❌   |
| 3   |    |     |      | a✅    | ab✅    | abc✅    | abcb❌    | abcbb❌    |
| 4   |    |     |      |       | b✅     | bc✅     | bcb❌     | bcbb❌     |
| 5   |    |     |      |       |        | c✅      | cb✅      | cbb❌      |
| 6   |    |     |      |       |        |         | b✅       | bb❌       |
| 7   |    |     |      |       |        |         |          | b✅        |

最大長度 = **3**（"abc", "bca", "cab"）。

---

要不要我幫你把這個流程畫成 **滑動視窗對照圖（格子移動方式）**，比上面表格更直觀？

太好了 👍 那我幫你把這段程式碼的運作流程畫成 **滑動視窗圖**，讓你直覺地看到「子字串檢查」的過程。

例子用：
`s = "abcabcbb"`

---

### 圖解流程

#### Step 1: i = 0

視窗從 `0` 開始往右擴展

```
[a] b c a b c b b   ✅ res = 1
[a b] c a b c b b   ✅ res = 2
[a b c] a b c b b   ✅ res = 3
[a b c a] b c b b   ❌ 'a' 重複
```

---

#### Step 2: i = 1

視窗從 `1` 開始往右擴展

```
a [b] c a b c b b   ✅ res = 1
a [b c] a b c b b   ✅ res = 2
a [b c a] b c b b   ✅ res = 3
a [b c a b] c b b   ❌ 'b' 重複
```

---

#### Step 3: i = 2

```
a b [c] a b c b b   ✅ res = 1
a b [c a] b c b b   ✅ res = 2
a b [c a b] c b b   ✅ res = 3
a b [c a b c] b b   ❌ 'c' 重複
```

---

#### Step 4: i = 3

```
a b c [a] b c b b   ✅ res = 1
a b c [a b] c b b   ✅ res = 2
a b c [a b c] b b   ✅ res = 3
a b c [a b c b] b   ❌ 'b' 重複
```

---

#### Step 5: i = 4

```
a b c a [b] c b b   ✅ res = 1
a b c a [b c] b b   ✅ res = 2
a b c a [b c b] b   ❌ 'b' 重複
```

---

#### Step 6: i = 5

```
a b c a b [c] b b   ✅ res = 1
a b c a b [c b] b   ✅ res = 2
a b c a b [c b b]   ❌ 'b' 重複
```

---

#### Step 7: i = 6

```
a b c a b c [b] b   ✅ res = 1
a b c a b c [b b]   ❌ 'b' 重複
```

---

#### Step 8: i = 7

```
a b c a b c b [b]   ✅ res = 1
```

---

### 結果

最大長度 `res = 3`
對應的最長子字串有：`"abc"`, `"bca"`, `"cab"`。

---

要不要我幫你畫成 **動畫 GIF 格子移動**（每一步滑動視窗），讓你更直觀地看到「指標 i、j 移動」的過程？

'''