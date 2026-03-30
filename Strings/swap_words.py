class Solution:
    def reverse_word_preserve_space(self,s):
        words=s.split()
        i=len(words)-1
        j=0
        result=[]
        while j<len(s):
            if s[j]==" ":
                result.append(s[j])
                j+=1
            else:
                while j<len(s) and s[j]!=" ":
                    j+=1
                result.append(words[i])
                i-=1
        return "".join(result)

s1=Solution()

s=" Hello world! "
print(s1.reverse_word_preserve_space(s))