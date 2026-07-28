class Soltuion:
    def product(self,nums):
        ans=[1]*len(nums)
        prefic=1
        for i in range(len(nums)):
            ans[i]=prefic
            prefic*=nums[i]
        
        sufix=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=sufix
            sufix*=nums[i]
        
        return ans

s1=Soltuion()
nums=[1,2,3,4]
print(s1.product(nums))