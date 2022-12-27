def partition(low,high,arr):
    key=arr[low]
    i=low
    j=high
    while (i<j) :
        while i<high and arr[i]<=key:
                i=i+1
        while arr[j]>key:
                j=j-1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
  
def quick_sort(low,high,arr):
    if low<high:
        p=partition(low,high,arr)
        quick_sort(low,p-1,arr)
        quick_sort(p+1,high,arr)
 
import random
Lis=[]
for j in range(5):
    l=[]
    for i in range(10):
        l.append(random.randint(-20,20))
    Lis.append(l)
for lists in Lis:
    quick_sort(0,len(lists)-1,lists)
Lis
