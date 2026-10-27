class Solution:
    def MedianOf2SortArray(self,nums1,nums2):
        m=len(nums1)
        n=len(nums2)
        if m==0 and n==0:
            return -1
        
        prev=0
        curr=0
        i=0
        j=0
        
        total=m+n
        for k in range(total//2+1):
            prev=curr
            
            if i<m and j<n:
                if nums1[i]<nums2[j]:
                    curr=nums1[i]
                    i+=1
                else:
                    curr=nums2[j]
                    j+=1
            
            elif i<m:
                curr=nums1[i]
                i+=1
                
            else:
                curr=nums2[j]
                j+=1
        
        if total%2==1:
            return float(curr)
        else:
            return (prev+curr)/2
s1=Solution()
print(s1.MedianOf2SortArray([1,4,5],[9,10,11]))
print(s1.MedianOf2SortArray([11,14,17],[3,4,5]))
print(s1.MedianOf2SortArray([11,14,15],[19,20,21]))