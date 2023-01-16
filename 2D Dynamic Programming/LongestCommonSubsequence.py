class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_table = [[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp_table[i][j] = 1 + dp_table[i-1][j-1]
                else:
                    #print(i, j)
                    dp_table[i][j] = max(dp_table[i][j-1], dp_table[i-1][j])
        #print(dp_table)
        return dp_table[-1][-1]