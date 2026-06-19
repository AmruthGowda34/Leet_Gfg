class soltuion:
    def frac_knap(self,nums,capacity):
        nums.sort(key=lambda x:x[0]/x[1],reverse=True)
        current_weight=0
        current_val=0
        for value,weight in nums:
            if current_weight+weight<=capacity:
                current_weight+=weight
                current_val+=value
            else:
                remain=capacity-current_weight
                current_val+=(value/weight)*remain
                break
        return current_val

s1=soltuion()
nums=[(100,20),(60,10),(100,50),(200,50)]
capacity=90
print(s1.frac_knap(nums,capacity))