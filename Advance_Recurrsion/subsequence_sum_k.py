class Solution:
    def fun(self, nums, ind, subset, result, tar, total):
        if total == tar:   #Backtracking 
            result.append(subset.copy())
            return
        
        if total > tar or ind >= len(nums):
            return
        
        subset.append(nums[ind])
        self.fun(nums, ind + 1, subset, result, tar, total + nums[ind])
        
        subset.pop()
        self.fun(nums, ind + 1, subset, result, tar, total)



s1 = Solution()
nums = [5, 9, 3, 4, 1]
tar = 9
result = []

s1.fun(nums, 0, [], result, tar, 0)
print(result)