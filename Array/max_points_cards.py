class SOlution:
    def cards(self,nums,k):
        left_sum=0
        right_sum=0
        max_points=0
        for i in range(0,k):
            left_sum+=nums[i]
        max_points=left_sum
        right_ind=len(nums)-1
        for i in range(k-1,-1,-1):
            left_sum-=nums[i]
            right_sum+=nums[right_ind]
            right_ind-=1
            max_points=max(max_points,left_sum+right_sum)
        return max_points
s1=SOlution()
nums=[1,2,3,4,5,6,1]
k = 3
print(s1.cards(nums,k))