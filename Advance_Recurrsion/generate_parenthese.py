class Soltuion:
    def generate_parn(self,ind,total,brackets,result):
        if ind==len(brackets):
            if total==0:
                result.append("".join(brackets))
            return
        if total>len(brackets)//2 or total<0:
            return 
        brackets[ind]="("
        sum=total+1
        self.generate_parn(ind+1,sum,brackets,result)
        brackets[ind]=")"
        sum=total-1
        self.generate_parn(ind+1,sum,brackets,result)
        
s1=Soltuion()
n=3
brackets=[""]*(n*2)
result=[]
s1.generate_parn(0,0,brackets,result)
print(result)

#OR


# class Solution:
#     def generateParenthesis(self, n: int):
#         result = []
#         brackets = [""] * (2 * n)

#         def solve(ind, open_count, close_count):
#             if ind == 2 * n:
#                 result.append("".join(brackets))
#                 return
            
#             if open_count < n:
#                 brackets[ind] = "("
#                 solve(ind + 1, open_count + 1, close_count)
            
#             if close_count < open_count:
#                 brackets[ind] = ")"
#                 solve(ind + 1, open_count, close_count + 1)

#         solve(0, 0, 0)
#         return result
# s1=Solution()
# n=3
# print(s1.generateParenthesis(n))