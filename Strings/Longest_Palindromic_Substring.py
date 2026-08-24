class Solution:
    def longest_pali_substring(self, s):
        start = 0
        max_len = 1

        for i in range(len(s)):

            # Even length
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    start = l

                l -= 1
                r += 1

            # Odd length
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                if r - l + 1 > max_len:  
                    max_len = r - l + 1
                    start = l

                l -= 1
                r += 1

        return s[start:start + max_len]


s1 = Solution()

print(s1.longest_pali_substring("babad"))