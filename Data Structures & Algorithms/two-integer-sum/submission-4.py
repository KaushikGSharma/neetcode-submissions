class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_num=sorted(enumerate(nums), key=lambda x:x[1])
        i=0
        j=len(sorted_num)-1
        while i<j:
            if sorted_num[i][1]+sorted_num[j][1]==target:
                return sorted([sorted_num[i][0],sorted_num[j][0]])
            elif sorted_num[i][1]+sorted_num[j][1]>target:
                j=j-1
            else:
                i=i+1
        return [-1,-1]