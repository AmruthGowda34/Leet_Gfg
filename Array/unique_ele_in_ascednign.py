class Solution:
    def fun(self,arr):
        count=1
        unique_count=0
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                count+=1
            else:
                if count==1:
                    unique_count+=1
                count=1
        if count==1:
            unique_count+=1
        
        print(unique_count)
    
    
s1=Solution()
arr=[1,2,3,4,5,6,7]
s1.fun(arr)
s1.fun([1,1,1,1,2,3])