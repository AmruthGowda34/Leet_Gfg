class Solution:
    def print_prime(self,n):
        count=0
        num=2
        while count<n:
            is_prime=True
            i=2
            while i*i<=num:
                if num%i==0:
                    is_prime=False
                    break
                i+=1
            if is_prime:
                print(num,end=" ")
                count+=1
            num+=1

s1=Solution()
s1.print_prime(10)  