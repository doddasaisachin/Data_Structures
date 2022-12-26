def linear_search(arr,ele):
    found=False
    for i in arr:
        if i==ele:
            found=True
    if found:
        print("element exist..!")
    if not found:
        print("element does'nt exist.")
