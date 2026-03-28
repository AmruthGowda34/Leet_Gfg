def Binary_Bakctrack(ind,flag,numbers,result):
    if ind>=len(numbers):
        result.append("".join(numbers))
        return
    numbers[ind]="0"
    Binary_Bakctrack(ind+1,True,numbers,result)
    if flag==True:
        numbers[ind]="1"
        Binary_Bakctrack(ind+1,False,numbers,result)
        numbers[ind]="0"
    return result

numbers=["0"]*3
result=[]
print(Binary_Bakctrack(0,True,numbers,result))