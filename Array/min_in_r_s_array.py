class Solution(object):
    def search(self,nums):
        low,high=0,len(nums)-1
        min_ele=float("inf")
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                min_ele=min(min_ele,nums[mid])
                high=mid-1
            else:
                min_ele=min(min_ele,nums[low])
                low=mid+1
        return min_ele
s1=Solution()
nums=[4,5,6,7,10,-1,0,1,2,3,3]
print(s1.search(nums))