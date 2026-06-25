class Soltuion:
    def min_plat(self,arrival,depar):
        arrival.sort()
        depar.sort()
        ans=1
        count=1
        i=1
        j=0
        while i<len(arrival) and j<len(depar):
            if arrival[i]<=depar[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            ans=max(ans,count)
        return ans
s1=Soltuion()
arrival = [900, 940, 950, 1100, 1500, 1800]
depar = [910, 1200, 1120, 1130, 1900, 2000]
print(s1.min_plat(arrival,depar))