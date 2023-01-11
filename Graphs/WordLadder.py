from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_dict = {word:True for word in wordList}
        visited_dict = {word:0 for word in wordList}
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        queue = deque()
        #Enter the first element
        queue.append((beginWord, 1))
        visited_dict[beginWord] = 1
        while queue:
            cur_word, level = queue[0]
            queue.popleft()
            if cur_word == endWord:
                return level
        
            chars = [ch for ch in cur_word]
            for ind in range(len(chars)):
                orig_char = chars[ind]
                for replacing_char in alphabet:
                    chars[ind] = replacing_char
                    checking_word = "".join(chars)
                    if checking_word in word_dict.keys() and  visited_dict[checking_word]==0:
                        visited_dict[checking_word]=1
                        queue.append((checking_word, level+1)) 
                chars[ind] = orig_char
        return 0    