class Solution:
    def next_grater_ele(self,n):
        stack=[]
        ans=[-1]*len(n)
        for i in range(2*len(n)-1,-1,-1):
            while stack and stack[-1]<=n[i%len(n)]:
                stack.pop()
            if i<len(n):
                if len(stack)!=0:
                    ans[i]=stack[-1]
            stack.append(n[i%len(n)])
        return ans

s1=Solution()
n=[2,10,12,1,11]
print(s1.next_grater_ele(n))