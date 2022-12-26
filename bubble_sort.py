def bubble_sort(List):
    for i in range(len(List)):
        for j in range(0,len(List)-i-1):
            if List[j]>List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
    return List
l=[9,0,7,1,-2,10,-8]
bubble_sort(l)
