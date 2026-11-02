class Solution:
    def ScoreOfParen(self,s):
        stack=[0]
        
        for ch in s:
            if ch=="(":
                stack.append(0)
                
            else:
                v=stack.pop()
                
                if v==0:
                    score=1
                else:
                    score=2*v
                
                stack[-1]+=score
            
        return stack[0]
s1=Solution()
print(s1.ScoreOfParen("()"))
print(s1.ScoreOfParen("(())"))
print(s1.ScoreOfParen("()()"))
print(s1.ScoreOfParen("(()(()))"))