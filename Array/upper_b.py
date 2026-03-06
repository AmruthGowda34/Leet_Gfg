n=[1,1,1,2,3,3,5,6,6,6,7,9,12,12,13]
u_b=len(n)
tar=9
low=0
high=len(n)-1
while low<=high:
    mid=(low+high)//2
    if n[mid]>tar:
        u_b=mid
        high=mid-1
    else:
        low=mid+1
print(u_b)
#upper_bound:-Smallest index shuch that n[mid]>tar value is called lower_bound
