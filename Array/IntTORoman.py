class SOlution:
    def IntTORom(self,num):
        integer=[
            (1000,"M"),
            (900,"CM"),
            (500,"D"),
            (400,"CD"),
            (100,"C"),
            (90,"XC"),
            (50,"L"),
            (40,"XL"),
            (10,"X"),
            (9,"IX"),
            (5,"V"),
            (4,"IV"),
            (1,"I")
        ]
        res=""
        for val,sym in integer:
            if num//val>0:
                count=num//val
                res+=count*sym
                num%=val
        
        return res


s1=SOlution()
print(s1.IntTORom(1947))
print(s1.IntTORom(7))
print(s1.IntTORom(49))
print(s1.IntTORom(9))