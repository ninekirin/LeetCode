#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.dict = {}

    def insert(self, word: str) -> None:
        if word not in self.dict:
            self.dict[word] = 1
        else:
            self.dict[word] += 1

    def search(self, word: str) -> bool:
        if word in self.dict:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for key in self.dict:
            if key.startswith(prefix):
                return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

