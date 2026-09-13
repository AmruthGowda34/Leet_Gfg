# class Solution:
#     def reverse_words(self,s):
#         result=[]
#         words=s.split()
#         for i in range(len(words)-1,-1,-1):
#             result.append(words[i])
#         return " ".join(result)
# s1=Solution()
# print(s1.reverse_words(" Hello this is AG"))
# print(s1.reverse_words(" The brand   "))


s=" Hello this is AG "
result=[]
words=""
for i in range(len(s)):
    if s[i]!=" ":
        words+=s[i]
    else:
        if words:
            result.insert(0,words)
            words=""
if words:
    result.insert(0,words)

print(" ".join(result))