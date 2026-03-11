class Solution:
    def rem(self,nums,tar):
        low=0
        high=len(nums)-1
        found=False
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==tar:
                nums.pop(mid)
                found=True
                return nums
            elif nums[mid]>tar:
                high=mid-1
            else:
                low=mid+1
        return "Element not in list!"
s1=Solution()
nums=[1,2,3,4,5,6]
print(s1.rem(nums,2))