# class Solution:
#     def fun(self,nums):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j]<nums[i]:
#                     nums[i],nums[j]=nums[j],nums[i]
#         return nums

# s1=Solution()
# nums = [2,0,2,1,1,0]
# print(s1.fun(nums))


class Soltuion:
    def sort_color(self,nums):
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums

s1=Soltuion()
nums = [2,0,2,1,1,0]
print(s1.sort_color(nums))