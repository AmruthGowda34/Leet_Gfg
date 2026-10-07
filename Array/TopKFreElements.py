class Solution():
    def topKele(self,nums,k):
        freq_map=dict()
        for i in range(len(nums)):
            freq_map[nums[i]]=freq_map.get(nums[i],0)+1
        
        sorted_nums=sorted(freq_map,key=freq_map.get,reverse=True)
        
        return sorted_nums[:k]
s1=Solution()
print(s1.topKele([1,2,1,2,1,2,3,1,3,2],2))
print(s1.topKele([1,1,1,2,2,3],2))
print(s1.topKele([1,2,1,2,1,2,3,1,3,2,4,4,4,4,5,5,5,5,5,5],2))