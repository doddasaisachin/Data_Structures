def merge_sorted_list(a,b,arr):
    len_a=len(a)
    len_b=len(b)
    i=j=k=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i=i+1
            k=k+1
        else:
            arr[k]=b[j]
            j=j+1
            k=k+1
    while i<len_a:
        arr[k]=a[i]
        i+=1
        k=k+1
    while j<len_b:
        arr[k]=b[j]
        j=j+1
        k=k+1
        
def merge_sort(arr):
    if len(arr)<=1:
        return
    mid = len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge_sorted_list(left,right,arr)
    
test=[
    [],
    [5],
    [1,9,5,7,3],
    [-1,0,-2,-3]
]

for i in test:
    (merge_sort(i))
    print(i)
 '''[]
    [5]
    [1, 3, 5, 7, 9]
    [-3, -2, -1, 0]'''
