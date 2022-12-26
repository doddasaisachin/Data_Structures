def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        ele=i-1
        while ele>=0 and key<arr[ele]:
            arr[ele+1]=arr[ele]
            ele=ele-1
        arr[ele+1]=key
    return arr
l=[9,0,7,1,-2,10,-8]
insertion_sort(l)
