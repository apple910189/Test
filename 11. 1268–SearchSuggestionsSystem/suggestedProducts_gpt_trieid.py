class TrieNode:
    def __init__(self):
        self.children = {}
        self.words_idx = []  # 存索引（最多3個）

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word_idx, products):
        word = products[word_idx]
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            # 插入索引，保持前三個最小字典序
            node.words_idx.append(word_idx)
            node.words_idx.sort()
            if len(node.words_idx) > 3:
                node.words_idx.pop()

    def search(self, prefix, products):
        node = self.root
        result = []
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
                result.append([products[i] for i in node.words_idx])
            else:
                # prefix 不存在，之後都補空列表
                while len(result) < len(prefix):
                    result.append([])
                break
        return result


class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()  # 確保字典序
        trie = Trie()

        # 建立 Trie
        for i in range(len(products)):
            trie.insert(i, products)

        # 搜尋每個 prefix
        return trie.search(searchWord, products)


sol = Solution()

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
ans = sol.suggestedProducts(products, searchWord)
print(ans)
