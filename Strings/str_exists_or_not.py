class Solution:
    def fun(self,str1,str2):
        freq={}
        for i in range(len(str1)):
            freq[str1[i]]=freq.get(str1[i],0)+1
        print(freq)
        for j in range(len(str2)):
            if str2[j] not in freq:
                print(f"{str2[j]}:exists")
            else:
                print(f"{str2[j]}:{freq[str2[j]]}")

s1=Solution()
str1="azyuyyzaaa"
str2="dayu"
s1.fun(str1,str2)