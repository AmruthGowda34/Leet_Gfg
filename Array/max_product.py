class Solution:
    def Array_Max_Product(self,nums):
        first=float("-inf")
        second=float("-inf")
        for i in nums:
            if i>first:
                second=first
                first=i
            elif i>second:
                second=i
        return (first-1)*(second-1)
s1=Solution()
nums = [3,4,5,2]
print(s1.Array_Max_Product(nums))