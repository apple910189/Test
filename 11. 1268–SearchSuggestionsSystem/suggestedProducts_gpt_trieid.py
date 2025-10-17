class TrieNode:
    def __init__(self):
        self.children = {}
        self.words_idx = []  # 存索引，不存字串

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
                while len(result) < len(prefix):
                    result.append([])
                break
        return result
