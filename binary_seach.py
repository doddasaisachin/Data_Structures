def binary_s(arr,low,high,ele):
    while high>=low:
        mid=(low+high)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]<ele:
            return binary_s(arr,mid+1,high,ele)
        else:
            return binary_s(arr,low,mid-1,ele)
    return -1
def binary_search(arr,ele):
    low = 0
    high=len(arr)-1
    result = binary_s(arr,low,high,ele)
    if result== -1:
        print("Element Not Found...!")
    else:
        print("element found at index :",result)
        
l=[6,0,8,-2,8]
binary_search(l,9)
