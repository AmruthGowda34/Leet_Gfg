class Solution:
    def ZigzagCon(self,s,numRows):
        if len(s)==0:
            return ""
        
        if numRows==0 or numRows>=len(s):
            return s
        
        rows=[""]*numRows
        curr_row=0
        direc=1
        
        for ch in s:
            rows[curr_row]+=ch
            
            if curr_row==0:
                direc=1
            
            elif curr_row==numRows-1:
                direc=-1
            
            curr_row+=direc
        
        return "".join(rows)
    
s1=Solution()
print(s1.ZigzagCon("PAYPALISHIRING",3))
print(s1.ZigzagCon("PAYPALISHIRING",4))
print(s1.ZigzagCon("A",1))