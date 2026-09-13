    # class Soltion:
#     def water(self,heights):
#         max_water=0
#         for i in range(len(heights)):
#             for j in range(i+1,len(heights)):
#                 width=j-i
#                 height=min(heights[i],heights[j])
#                 max_water=max(max_water,width*height)
#         return max_water

# s1=Soltion()
# heights = [1,8,6,2,5,4,8,3,7]
# print(s1.water(heights))

class Solutuion:
    def water(self,height):
        left=0
        right=len(height)-1
        max_water=0
        while left<right:
            w=right-left
            h=min(height[left],height[right])
            max_water=max(max_water,w*h)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        return max_water

s1=Solutuion()
height = [1,8,6,2,5,4,8,3,7]
print(s1.water(height))