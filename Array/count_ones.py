class Soltuion:
    def one(self,nums):
        count=0
        maxi_count=float("-inf")
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                maxi_count=max(maxi_count,count)
                count=0
        return max(maxi_count,count)

s1=Soltuion()
nums=[1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1]

print(s1.one(nums))