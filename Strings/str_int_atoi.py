class Solution(object):
    def myAtoi(self, s):
        i = 0

        # Skip leading spaces
        while i < len(s) and s[i] == " ":
            i += 1

        # Sign
        sign = 1

        if i < len(s) and s[i] == "+":
            i += 1

        elif i < len(s) and s[i] == "-":
            sign = -1
            i += 1

        # Convert digits
        num = 0

        while i < len(s) and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        num *= sign

        # 32-bit range
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if num > INT_MAX:
            return INT_MAX

        if num < INT_MIN:
            return INT_MIN

        return num

s1=Solution()

print(s1.myAtoi("1337c0d3"))

# 1. Remove leading spaces
# 2. Check for + or -
# 3. Read digits
# 4. Stop when a non-digit is encountered
# 5. Apply the sign
# 6. Handle 32-bit integer limits