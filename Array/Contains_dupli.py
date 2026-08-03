class Solution:
    def contain_dupli(self,nums):
        a=set()
        for i in range(len(nums)):
            if nums[i] in a:
                return True
            a.add(nums[i])
        return False


s1=Solution()
nums = [1,2,3,1]
print(s1.contain_dupli(nums))
print(s1.contain_dupli([1,2,3,4]))


# def fun(nums):
#     nums.sort()
#     for i in range(len(nums)-1):
#         if nums[i]==nums[i+1]:
#             return True
#     return False
# nums=[1,2,3,1]
# print(fun(nums))