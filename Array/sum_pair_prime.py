class Solution:
    def is_prime(self,n):
        if n<=1:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
    
    def prime_pair(self,arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                pair_sum=arr[i]+arr[j]
                if self.is_prime(pair_sum):
                    print(arr[i],arr[j])
s1=Solution()
arr=[1,4,2,7,5,3]
s1.prime_pair(arr)