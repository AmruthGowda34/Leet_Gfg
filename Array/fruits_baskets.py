class Solution:
    def fru_baskeet(self,fruits):
        
        #-----------Bruteforce---------------
        # max_len=float("-inf")
        # for i in range(len(fruits)):
        #     basket=set()
        #     for j in range(i,len(fruits)):
        #         basket.add(fruits[j])
        #         if len(basket)>2:
        #             break
        #         max_len=max(max_len,j-i+1)
        # return max_len
        
        #-----------Optimaal-----------------
        left=0
        right=0
        my_dict={}
        max_len=float("-inf")
        while right<len(fruits):
            my_dict[fruits[right]]=my_dict.get(fruits[right],0)+1
            if len(my_dict)>2:
                my_dict[fruits[left]]-=1
                if my_dict[fruits[left]]==0:
                    del my_dict[fruits[left]]
                left+=1
            max_len=max(max_len,right-left+1)
            right+=1
        return max_len
    
s1=Solution()
fruits=[3,3,3,1,2,1,1,2,3,3,4]
print(s1.fru_baskeet(fruits))
print(s1.fru_baskeet([0,1,2,2]))