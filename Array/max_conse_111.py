class SOlution:
    def long(self,nums,k):
        
        #-------------Bruteforce------------
        # max_len=0
        # for i in range(len(nums)):
        #     zeros=0
        #     for j in range(i,len(nums)):
        #         if nums[j]==0:
        #             zeros+=1
        #         if zeros>k:
        #             break
        #         max_len=max(max_len,j-i+1)
        # return max_len
        
        
        #---------Optimal----------------
        max_len=0
        left=0
        right=0
        zeros=0
        while right<len(nums):
            if nums[right]==0:
                zeros+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            if zeros<=k:
                max_len=max(max_len,right-left+1)
            right+=1
        return max_len

s1=SOlution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(s1.long(nums,k))
print(s1.long([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))