# class Solution:
#     def fun(self,nums):
#         map={}
#         for i in range(len(nums)):
#             if nums[i] in map:
#                 map[nums[i]]=map.get(nums[i],0)+1
#             else:
#                 map[nums[i]]=1
#         for k,v in map.items():
#             if v>len(nums)//2:
#                 return k
#         return -1
# s1=Solution()
# nums = [2,2,1,1,1,2,2]
# print(s1.fun(nums))


class Solution:
    def fun(self,nums):
        candidate=None
        count=0
        for i in nums:
            if count==0:
                candidate=i
            if i==candidate:
                count+=1
            else:
                count-=1
        return candidate

s1=Solution()
nums=[2,2,1,1,1,2,2]
print(s1.fun(nums))