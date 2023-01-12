class WordDictionary:

    def __init__(self):
        self.word_dict = {}

    def addWord(self, word: str) -> None:
        cur_dict = self.word_dict
        for ind, char in enumerate(word):
            if char not in cur_dict.keys():
                cur_dict[char] = [{}, False]
            if ind==len(word)-1:
                cur_dict[char][1] = True
            cur_dict = cur_dict[char][0]

    def searchword(self, word, cur_dict, ind):
        chars = word[ind]
        if chars==".":
            chars="qwertyuiopasdfghjklzxcvbnm"
        if len(word)==ind+1:
            for char in chars:
                if char in cur_dict.keys() and cur_dict[char][1]:
                    return True
            return False
        for char in chars:
            if char in cur_dict.keys() and self.searchword(word, cur_dict[char][0], ind+1):
                return True

        return False


    def search(self, word: str) -> bool:
        return self.searchword(word, self.word_dict, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)