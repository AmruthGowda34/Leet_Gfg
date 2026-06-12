class SOlution:
    def asteroid(self,nums):
        stack=[]
        for i in range(len(nums)):
            if nums[i]>0:
                stack.append(nums[i])
            else:
                while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(nums[i]):
                    stack.pop()
                if len(stack)!=0 and stack[-1]==abs(nums[i]):
                    stack.pop()
                elif len(stack)==0 or stack[-1]<0:
                    stack.append(nums[i])
        return stack

s1=SOlution()
nums=[4,7,1,1,-3,-7,17,15,-18,-19]
print(s1.asteroid(nums))