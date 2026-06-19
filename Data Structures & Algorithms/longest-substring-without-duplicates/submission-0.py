from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        max_len=float('-inf')
        wind_max_len=0
        start=0
        end=0
        state=defaultdict(int)
        while end<len(s):
            state[s[end]]+=1
            if end-start+1 == len(state):
                max_len=max(max_len,end-start+1)
            else:
                while end-start+1 > len(state) and start<=end:
                    state[s[start]]-=1
                    if state[s[start]]==0:
                        del state[s[start]]
                    start+=1
            end+=1
        return max_len
