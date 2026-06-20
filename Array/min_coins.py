class Soltuion:
    def minmum_coins(self,coins,n):
        min_coins=[]
        for i in range(len(coins)-1,-1,-1):
            while n>=coins[i]:
                min_coins.append(coins[i])
                n-=coins[i]
        return min_coins   

s1=Soltuion()
coins=[1,2,5,10,20,50,100,200,500,2000]
n=47
print(s1.minmum_coins(coins,n))