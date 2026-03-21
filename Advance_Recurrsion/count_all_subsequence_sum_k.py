class Solution:
    def back_tr(self,ind,nums,total,k):
        if total==k:
            return 1
        if total>k or ind>=len(nums):
            return 0
        sum=total+nums[ind]
        pick=self.back_tr(ind+1,nums,sum,k)
        sum=total
        not_pick=self.back_tr(ind+1,nums,sum,k)
        return pick+not_pick

s1=Solution()
nums=[5,9,4]
print(s1.back_tr(0,nums,0,9))