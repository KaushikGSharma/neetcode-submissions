class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        min_now=nums[0]
        sorted_right_ind=r
        sorted_left_ind=l
        while l<=r:
            m=l+(r-l)//2
            min_now=min(nums[m],min_now)
            if nums[l]<=nums[r] and nums[m]>=nums[l] and nums[m]<=nums[r]:
                r=m-1
                l=sorted_left_ind
                sorted_right_ind=m-1
            elif nums[l]>nums[r]:
                if nums[m]>=nums[l]:
                    l=m+1
                    sorted_left_ind=m+1
                    r=sorted_right_ind
                elif nums[m]<=nums[r]:
                    r=m-1
                    l=sorted_left_ind
                    sorted_right_ind=m-1
        return min_now



