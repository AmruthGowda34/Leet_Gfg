class Solution:
    def swap_vowels(self,s):
        s=s.lower()
        vowels=set("aeiou")
        s_set=list(s)
        l,r=0,len(s)-1
        while l<r:
            if s_set[l] not in vowels:
                l+=1
            elif s_set[r] not in vowels:
                r-=1
            else:
                s_set[l],s_set[r]=s_set[r],s_set[l]
                l+=1
                r-=1
        return "".join(s_set)
s1=Solution()
print(s1.swap_vowels("Hello"))