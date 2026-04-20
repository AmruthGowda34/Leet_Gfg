class Soltion:
    def water(self,heights):
        max_water=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                width=j-i
                height=min(heights[i],heights[j])
                max_water=max(max_water,width*height)
        return max_water

s1=Soltion()
heights = [1,8,6,2,5,4,8,3,7]
print(s1.water(heights))