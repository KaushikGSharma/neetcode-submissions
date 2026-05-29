class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num=set()
        for i in nums:
            unique_num.add(i)
        if len(unique_num) != len(nums):
            return True
        return False
        