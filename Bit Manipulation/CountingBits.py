class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_count = [0]

        for i in range(1,n+1):
            if i&1:
                bit_count.append(bit_count[-1]+1)
            else:
                bit_count.append(bit_count[i//2])
        return bit_count