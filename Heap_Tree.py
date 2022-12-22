def heapify(arr,i):
    largest=i
    l=2*i+1
    r=2*i+2
    
    if l<len(arr) and arr[l]>arr[largest]:
        largest=l
    if r<len(arr) and arr[r]>arr[largest]:
        largest=r
    if (largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,largest)
        
def insertNode(arr,node):
    if len(arr)==0:
        arr.append(node)
    arr.append(node)
    for i in range(len(arr)):
        heapify(arr,i)
        
def deleteNode(arr,node):
    for i in range(len(arr)):
        if arr[i]==node:
            break
    arr[i],arr[len(arr)-1]=arr[len(arr)-1],arr[i]
    arr.remove(node)
    for i in range(len(arr)):
        heapify(arr,i)
        
