class SOlution:
    def decode_str(self,s):
        stack=[]
        current_str=""
        current_num=0
        for ch in s:
            if ch.isdigit():
                current_num=current_num*10+int(ch)
            
            elif ch=="[":
                stack.append((current_str,current_num))
                current_str=""
                current_num=0
            
            elif ch=="]":
                prev_str,repeat=stack.pop()
                current_str=prev_str+current_str*repeat
            
            else:
                current_str+=ch
            
        return current_str

s1=SOlution()
print(s1.decode_str("3[a2[c]]"))
print(s1.decode_str("3[a]2[bc]"))
print(s1.decode_str("2[abc]3[cd]ef"))