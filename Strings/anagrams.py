class Solution:
    def anagram(self,str1,str2):
        
        str1=str1.replace(" ","").lower()
        str2=str2.replace(" ","").lower()
        
        if len(str1)!=len(str2):
            return False
        size=[0]*26
        for i in range(len(str1)):
            size[ord(str1[i])-ord('a')]+=1
            size[ord(str2[i])-ord('a')]-=1
        return all(c==0 for c in size)
s1=Solution()
print(s1.anagram("Listen"," silent"))
print(s1.anagram("ARC","car"))
print(s1.anagram("care","race"))