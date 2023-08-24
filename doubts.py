#2563. Count the Number of Fair Pairs

nums=[0,1,7,4,4,5]
nums.sort()#
lower = 3
upper = 6
c=0
for i in range(len(nums)-1):
    lo=i+1
    hi=len(nums)-1
    while(lo<=hi):
        mid=(lo+hi)//2
        if nums[i]+nums[mid] >=lower and nums[i]+nums[mid] <=upper:
            left_index=mid
            right_index=mid
            while(left_index>lo and (nums[i]+nums[left_index -1])>=lower ):
                left_index=left_index-1
            while(right_index <len(nums)-1 and(nums[i]+nums[right_index+1])<=upper):
                right_index=right_index+1
            c+= (right_index-left_index)+1
            break
        if nums[i]+nums[mid]<lower:
            lo = mid+1
        if nums[i]+nums[mid]>upper:
            hi = mid-1
print(c)


