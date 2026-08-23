class Solution:
    def Valid_Palin(self,s):
        left=0
        right=len(s)-1
        
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            
            left+=1
            right-=1
        
        return True

s1=Solution()
print(s1.Valid_Palin("A man, a plan, a canal: Panama"))
print(s1.Valid_Palin("12321"))
print(s1.Valid_Palin("race a car"))