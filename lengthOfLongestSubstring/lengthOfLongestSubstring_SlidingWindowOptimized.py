class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # charToNextIndex stores the index after current character
        charToNextIndex = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1

        return ans

sol = Solution()
res = sol.lengthOfLongestSubstring('aab')
print(res)

'''
好的，我幫你用**流程圖 + 視覺化範例**來解釋這段程式。
這是 LeetCode 經典題 **Longest Substring Without Repeating Characters** 的 **滑動視窗 (Sliding Window)** 解法。

---

## 1. 程式流程圖

```
輸入字串 s
       │
       ▼
初始化 n = len(s), ans = 0, charToNextIndex = {}, i = 0
       │
       ▼
for j in range(n):   ←─ 掃描每個字元
       │
       ├─► 檢查 s[j] 是否出現在 charToNextIndex
       │        │
       │        ├─ 是 → i = max(charToNextIndex[s[j]], i)
       │        └─ 否 → 不動
       │
       ├─ 更新當前視窗長度 ans = max(ans, j - i + 1)
       │
       └─ 記錄字元下次可用位置 charToNextIndex[s[j]] = j + 1
       │
       ▼
迴圈結束
       │
       ▼
回傳 ans
```

---

## 2. 視覺化範例

假設輸入字串：

```
s = "abcabcbb"
```

### Step by Step

1. **初始化**

   * i = 0, ans = 0, charToNextIndex = {}

---

2. **j = 0, s\[j] = 'a'**

   * 'a' 不在 dict
   * ans = max(0, 0 - 0 + 1) = 1
   * dict = {'a': 1}

   視窗 = `[a]`

---

3. **j = 1, s\[j] = 'b'**

   * 'b' 不在 dict
   * ans = max(1, 1 - 0 + 1) = 2
   * dict = {'a': 1, 'b': 2}

   視窗 = `[a b]`

---

4. **j = 2, s\[j] = 'c'**

   * 'c' 不在 dict
   * ans = max(2, 2 - 0 + 1) = 3
   * dict = {'a': 1, 'b': 2, 'c': 3}

   視窗 = `[a b c]`

---

5. **j = 3, s\[j] = 'a'**

   * 'a' 在 dict，且 dict\['a'] = 1
   * i = max(1, 0) = 1
   * ans = max(3, 3 - 1 + 1) = 3
   * dict\['a'] = 4

   視窗 = `[b c a]`

---

6. **j = 4, s\[j] = 'b'**

   * 'b' 在 dict，dict\['b'] = 2
   * i = max(2, 1) = 2
   * ans = max(3, 4 - 2 + 1) = 3
   * dict\['b'] = 5

   視窗 = `[c a b]`

---

7. **j = 5, s\[j] = 'c'**

   * 'c' 在 dict，dict\['c'] = 3
   * i = max(3, 2) = 3
   * ans = max(3, 5 - 3 + 1) = 3
   * dict\['c'] = 6

   視窗 = `[a b c]`

---

8. **j = 6, s\[j] = 'b'**

   * 'b' 在 dict，dict\['b'] = 5
   * i = max(5, 3) = 5
   * ans = max(3, 6 - 5 + 1) = 2
   * dict\['b'] = 7

   視窗 = `[c b]`

---

9. **j = 7, s\[j] = 'b'**

   * 'b' 在 dict，dict\['b'] = 7
   * i = max(7, 5) = 7
   * ans = max(3, 7 - 7 + 1) = 1
   * dict\['b'] = 8

   視窗 = `[b]`

---

✅ 最終答案：`ans = 3`
對應到最長的不重複子字串 `"abc"`。

---

要不要我幫你畫成 **圖解動畫（移動視窗的過程圖）**，讓你一眼看到左右指標 `i` 和 `j` 是怎麼移動的？


'''