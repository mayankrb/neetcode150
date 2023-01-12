class Trie:

    def __init__(self):
        self.word_dict={}

    def insert(self, word: str) -> None:
        cur_dict = self.word_dict
        for ind, char in enumerate(word):
            if char not in cur_dict.keys():
                cur_dict[char] = [{}, False]
            if ind==len(word)-1:
                cur_dict[char][1] = True
            cur_dict = cur_dict[char][0]

    def searchword(self, word, cur_dict, ind, start_with_flag):
        chars = word[ind]
        if len(word)==ind+1:
            for char in chars:
                if char in cur_dict.keys() and (start_with_flag or cur_dict[char][1]):
                    return True
            return False
        for char in chars:
            if char in cur_dict.keys() and self.searchword(word, cur_dict[char][0], ind+1, start_with_flag):
                return True

        return False


    def search(self, word: str) -> bool:
        return self.searchword(word, self.word_dict, 0, False)   

    def startsWith(self, prefix: str) -> bool:
        return self.searchword(prefix, self.word_dict, 0, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)