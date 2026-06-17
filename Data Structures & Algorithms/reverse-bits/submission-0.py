class Solution:
    def reverseBits(self, n: int) -> int:
        i=0
        result=0
        while i<32:
            if (n>>i)&1 == 1:
                result = result | (1<< (31-i))
            i+=1
        return result