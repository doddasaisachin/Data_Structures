def selection_sort(List):
    for i in range(len(List)):
        min_index=i
        for j in range(i+1,len(List)):
            if List[j]<List[min_index]:
                min_index=j
        List[i],List[min_index]=List[min_index],List[i]
    return List
l=[9,0,7,1,-2,10,-8]
selection_sort(l)
