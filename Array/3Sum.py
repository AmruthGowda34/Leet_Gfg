class Solution:
    def ThreeSum(self,nums):
        
        #Brute Forces 
        # my_set=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 res=[nums[i],nums[j],nums[k]]
        #                 res.sort()
        #                 my_set.add(tuple(res))
        # return [list(ans) for ans in my_set]
        
        # res=set()
        # for i in range(len(nums)):
        #     my_set=set()
        #     for j in range(i+1,len(nums)):
        #         k=-(nums[i]+nums[j])
        #         if k in my_set:
        #             temp=[nums[i],nums[j],k]
        #             temp.sort()
        #             res.add(tuple(temp))
        #         my_set.add(nums[j])
        # return [list(ans) for ans in res]
        
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    j += 1

                elif total_sum > 0:
                    k -= 1

                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans

s1=Solution()
print(s1.ThreeSum([-1,0,1,2,-1,-4]))