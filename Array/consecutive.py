class solution:
    def fun(self,nums):
        my_set=set(nums)
        maxi=0
        for i in my_set:
            if i-1 not in my_set:
                number=i
                count=1
                while number+1 in my_set:
                    count+=1
                    number+=1
                maxi=max(maxi,count)
        return maxi

s1=solution()
nums=[0,3,7,2,5,8,4,6,0,1]
print(s1.fun(nums))
