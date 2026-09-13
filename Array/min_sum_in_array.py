class Solution:
    def fun(self,arr):
        min_sum=float('inf')
        a=0
        b=1
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]<min_sum:
                    min_sum=arr[i]+arr[j]
                    a=i
                    b=j
        print(arr[a],arr[b])
    
s1=Solution()
arr=[2,4,6,3,8,9]
s1.fun(arr)