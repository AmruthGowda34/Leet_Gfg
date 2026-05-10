class Solution:
    def fun(self,s):
        stack=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                ch=stack.pop()
                if (i==")" and ch=="(") or (i=="]" and ch=="[") or (i== "}" and ch=="{"):
                    continue
                else:
                    return False
        
        return len(stack)==0

s1=Solution()
print(s1.fun("(())"))            
print(s1.fun("(())["))            