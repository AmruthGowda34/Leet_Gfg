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
print(s1.subarray_sum_equals_k([1,2,3,-3,1,1,1,4,4,-3],3))

# n=[1,2,3,-3,1,1,1,4,4,-3]
# k=3
# count=0
# for i in range(len(n)):
#     summ=0
#     for j in range(i,len(n)):
#         summ+=n[j]
#         if summ==k:
#             count+=1
# print(count)