
class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        result = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            suggestions = []
            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)
            result.append(suggestions[:3])
        return result



sol = Solution()


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
ans = sol.suggestedProducts(products, searchWord)
print(ans)