from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Your code goes here
        if len(s)==0:
            return 0
        max_len=float('-inf')
        state=defaultdict(int)
        start=0
        end=0
        max_freq=0
        while end<len(s):
            state[s[end]]+=1
            max_freq=max(max_freq,state[s[end]])
            if (end-start+1)-max_freq<=k:
                max_len=max(max_len,end-start+1)
            else:
                while (end-start+1)-max_freq>k and start<=end:
                    state[s[start]]-=1
                    if state[s[start]]==0:
                        del state[s[start]]
                    start+=1
            end+=1
        return max_len
