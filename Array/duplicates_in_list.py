class Solution:
    def duplicates(self,nums):
        freq_map={}
        for i in range(len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]]+=1
            else:
                freq_map[nums[i]]=1
        return freq_map

s1=Solution()
nums=[1,1,2,5,9,7,2,1,6,7,7,3,4,3,2,2,1]        
print(s1.duplicates(nums))