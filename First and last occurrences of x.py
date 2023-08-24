# First and last occurrences of x
# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/0

def find(arr,n,x):
    # code here
    lo=0
    hi=n-1
    while(lo<=hi):
        mid=(lo+hi)//2
        if arr[mid]==x:
            left_index=mid
            right_index=mid
            while(left_index>0 and arr[left_index -1]==arr[mid] ):
                left_index=left_index-1
            while(right_index <n-1 and arr[right_index+1]==arr[mid]):
                right_index=right_index+1
            return left_index,right_index
        else:
            if arr[mid]<x:
                lo=mid+1
            else:
                hi=mid-1
    return -1,-1
