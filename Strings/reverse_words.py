class Solution:
    def reverse_words(self,s):
        result=[]
        word=""
        for ch in s:
            if ch!=" ":
                word+=ch
            else:
                if word:
                    result.insert(0,word)
                    word=""
        if word:
            result.insert(0,word)
        return " ".join(result)

s1=Solution()
print(s1.reverse_words(" Hello this is AG"))
print(s1.reverse_words(" The brand   "))