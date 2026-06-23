class Soltuion:
    def can_jump(self,nums):
        max_ind=0
        for i in range(len(nums)):
            if i>max_ind:
                return False
            max_ind=max(max_ind,i+nums[i])
        return True
s1=Soltuion()
nums=[2,3,1,1,4]
print(s1.can_jump(nums))
print(s1.can_jump([3,2,1,0,4]))