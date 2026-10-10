class Solution:
    def InterSecOfArray(self,num1,num2):
        # num1.sort()
        # num2.sort()
        
        # res=[]
        # i,j=0,0
        # while i<len(num1) and j<len(num2):
        #     if num1[i]<num2[j]:
        #         i+=1
        #     elif num2[j]<num1[i]:
        #         j+=1
        #     else:
        #         if len(res)==0 or res[-1]!=num1[i]:
        #             res.append(num1[i])
        #         i+=1
        #         j+=1
        
        # return res
        
        #Without sorting
        
        return list(set(num1)&set(num2))

s1=Solution()
num1 = [4,9,5]
num2 = [9,4,9,8,4]
print(s1.InterSecOfArray(num1,num2))