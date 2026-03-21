def longest_sub_string(str):
    seen=set()
    l=0
    max_length=0
    for r in range(len(str)):
        while str[r] in seen:
            seen.remove(str[l])
            l+=1
        seen.add(str[r])
        max_length=max(max_length,r-l+1)
    return max_length
    
print(longest_sub_string("abccbacbccad"))
print(longest_sub_string("abcdabccbafg"))