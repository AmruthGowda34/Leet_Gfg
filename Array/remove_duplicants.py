class Solution:
    def rem_duplicants(self,nums,k):
        # result=[]
        # for i in nums:
        #     if i!=k:                 #Time_complexity:o(n)
        #         result.append(i)     #Space_complexity:O(n)
        # return result
        # for i in range(len(nums)):    Time_complexity:O(n^2)
        #     if k in nums:             Space_complexiyt:O(1)
        #         nums.remove(k)
        # return nums
        i=0
        for j in range(len(nums)):      #Time_complexity:O(n)
            if nums[j]!=k:              #Space_complexity:O(1)
                nums[i]=nums[j]
                i+=1
        return nums[:i]
s1=Solution()
nums=[1,2,2,2,2,2,4,5,6,6,7]
print(s1.rem_duplicants(nums,2))