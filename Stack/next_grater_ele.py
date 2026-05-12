# n=[19,4,2,11,6,5,3,10]
# ans=[]
# for i in range(len(n)):
#     found=-1
#     for j in range(i+1,len(n)):
#         if n[j]>n[i]:
#             found=n[j]
#             break
#     ans.append(found)
# print(ans)

#---------------------------------------------------------

# n=[19,4,2,11,6,5,3,10]
# ans=[-1]*len(n)
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[j]>n[i]:
#             ans[i]=n[j]
#             break
# print(ans)

#----------------------------------------------------------

class Solution:
    def fun(self,nums):
        stack=[]
        ans=[-1]*len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            
            stack.append(nums[i])
        
        return ans

s1=Solution()
print(s1.fun([19,4,2,11,6,5,3,10]))