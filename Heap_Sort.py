def heapify(ele,size,arr):
    largest=ele
    left=2*ele+1
    right=2*ele+2
    if left<size and arr[left]>arr[ele]:
        largest=left
    if right<size and arr[right]>arr[largest]:
        largest=right
    if largest!=ele:
        arr[ele],arr[largest]=arr[largest],arr[ele]
        heapify(largest,size,arr)
        
def heap_sort(arr):
    size=len(arr)
    for i in range(size//2,-1,-1):
        heapify(i,size,arr)
    for i in range(size-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(0,i,arr)
    return arr 
  
  
