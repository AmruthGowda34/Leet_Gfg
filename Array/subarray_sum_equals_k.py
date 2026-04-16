class Solution:
    def subarray_sum_equals_k(self,nums,k):
        pre_sum=0
        count=0
        hash_map={0:1}
        for i in nums:
            pre_sum+=i
            if pre_sum-k in hash_map:
                count+=hash_map[pre_sum-k]
            hash_map[pre_sum]=hash_map.get(pre_sum,0)+1
        return count

s1=Solution()
nums=[1,2,3]
k=3
print(s1.subarray_sum_equals_k(nums,k))