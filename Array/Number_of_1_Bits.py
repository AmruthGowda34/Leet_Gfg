class Solution(object):
    def hammingWeight(self, n):
        # if n==0:
        #     return 0
        # result=""
        # while n>0:
        #     result+=str(n%2)
        #     n//=2
        # result=result[::-1]
        # count=0
        # for i in range(len(result)):
        #     if int(result[i])==1:
        #         count+=1
        # return count
        
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count

s1=Solution()
print(s1.hammingWeight(11))    