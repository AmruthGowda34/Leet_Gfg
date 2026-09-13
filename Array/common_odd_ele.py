class Solution:
    def fun(self,arr1,arr2):
        i=0
        j=0
        result=[]
        while i<len(arr1) and j<len(arr2):
            if arr1[i]==arr2[j]:
                if arr1[i]%2!=0:
                    if not result or result[-1]!=arr1[i]:
                        result.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i]<arr2[j]:
                i+=1
            else:
                j+=1
        
        if result:
            print(*(result))
        else:
            print("No odd elements.")
s1=Solution()
arr1=[1,2,3,4,5]
arr2=[3,4,5,6,7]
s1.fun(arr1,arr2)