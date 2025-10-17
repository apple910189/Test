class Solution:

    class TrieNode:
        def __init__(self):
            self.nextNode = [None] * 26
            self.suggestedProductsId = []

    def __init__(self):
        self.root = self.TrieNode()
        self.products = []

    def lowerCaseToIndex(self, c):
        return ord(c) - ord('a')

    # add a word to trie
    def add(self, node, product, productId, index):
        if len(node.suggestedProductsId) < 3:
            node.suggestedProductsId.append(productId)
        if index == len(product):
            return
        nextIndex = self.lowerCaseToIndex(product[index])
        if node.nextNode[nextIndex] is None:
            node.nextNode[nextIndex] = self.TrieNode()
        self.add(node.nextNode[nextIndex], product, productId, index + 1)

    def search(self, node, searchPhrases, index, answer):
        if node != self.root:
            lst = [self.products[i] for i in node.suggestedProductsId]
            answer.append(lst)
        if index == len(searchPhrases):
            return
        nextIndex = self.lowerCaseToIndex(searchPhrases[index])
        if node.nextNode[nextIndex] is not None:
            self.search(node.nextNode[nextIndex], searchPhrases, index + 1, answer)
        else:
            for _ in range(index + 1, len(searchPhrases) + 1):
                answer.append([])

    def init(self, products):
        self.root = self.TrieNode()
        self.products = sorted(products)
        for i, product in enumerate(self.products):
            self.add(self.root, product, i, 0)

    def query(self, searchPhrases):
        answer = []
        self.search(self.root, searchPhrases, 0, answer)
        return answer


sol = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
sol.init(products)
ans = sol.query(searchWord)
print(ans)



'''
0: mobile
1: moneypot
2: monitor
3: mouse
4: mousepad

(root)
 └─ m : [0, 1, 2]        # "mobile","moneypot","monitor"
     └─ o : [0, 1, 2]    # "mobile","moneypot","monitor"
         ├─ b : [0]      # "mobile"
         │    └─ i : [0]
         │         └─ l : [0]
         │              └─ e : [0]
         ├─ n : [1, 2]   # "moneypot","monitor"
         │    ├─ e : [1]
         │    │    └─ y : [1]
         │    │         └─ p : [1]
         │    │              └─ o : [1]
         │    │                   └─ t : [1]
         │    └─ i : [2]
         │         └─ t : [2]
         │              └─ o : [2]
         │                   └─ r : [2]
         └─ u : [3, 4]   # "mouse","mousepad"
              └─ s : [3, 4]
                   └─ e : [3, 4]
                        └─ p : [4]
                             └─ a : [4]
                                  └─ d : [4]

'''



