class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()  # optimization

        def backtrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                # 🚫 Pruning (important optimization)
                if candidates[i] > target:
                    break
                
                # ✅ Choose element
                path.append(candidates[i])
                
                # Stay at same index (reuse allowed)
                backtrack(i, target - candidates[i], path)
                
                # 🔁 Backtrack
                path.pop()

        backtrack(0, target, [])
        return result


# Test
s = Solution()
print(s.combinationSum([2,3,6,7], 7))