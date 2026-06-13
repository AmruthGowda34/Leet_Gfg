def longest_sub_string(str):
    
    #------------Bruteforce-------------------------
    # max_len=float('-inf')
    # for i in range(len(str)):
    #     my_set=set()
    #     for j in range(i,len(str)):
    #         if str[j] in my_set:
    #             break
    #         max_len=max(max_len,j-i+1)
    #         my_set.add(str[j])
    # return max_len


    #----------Optimal-------------------------
    max_len=float('-inf')
    l=0
    seen=set()
    for r in range(len(str)):
        while str[r] in seen:
            seen.remove(str[l])
            l+=1
        max_len=max(max_len,r-l+1)
        seen.add(str[r])
    return max_len
    
        
print(longest_sub_string("abcdabccbafg"))
print(longest_sub_string("CADBZABCDE"))