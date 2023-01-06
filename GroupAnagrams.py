class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_dict = {}
        anagrams_final_list = []
        
        for cur_str in strs:
            key = "".join(sorted(cur_str))
            try:
                anagrams_dict[key].append(cur_str)
            except:
                anagrams_dict[key] = [cur_str]
        
        for key, cur_anagram_list in anagrams_dict.items():
            anagrams_final_list.append(cur_anagram_list)
        
        return anagrams_final_list