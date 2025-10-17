class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []  # 這個節點以下的字（最多三個）

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.words.append(word)
            node.words.sort()
            if len(node.words) > 3:
                node.words.pop()

    def search(self, prefix):
        node = self.root
        result = []
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
                result.append(node.words)
            else:
                # 找不到的話後面全是空清單
                while len(result) < len(prefix):
                    result.append([])
                break
        return result

class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for product in sorted(products):  # 先排序，確保字典序正確
            trie.insert(product)
        return trie.search(searchWord)


sol = Solution()


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
ans = sol.suggestedProducts(products, searchWord)
print(ans)


trie = Trie()

for product in ["mobile","mouse","moneypot","monitor","mousepad"]:
    trie.insert(product)

def print_trie(node, prefix=""):
    # 印出目前節點的 prefix 與 words
    if node.words:
        print(f"Prefix: '{prefix}' -> words: {node.words}")
    # 遞迴印出 children
    for ch, child in node.children.items():
        print_trie(child, prefix + ch)

# print_trie(trie.root)
print(trie.root.words)





