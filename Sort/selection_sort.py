def sel_sort(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i+1,len(arr)):
            if(arr[min]>arr[j]):
                min=j
        
        arr[i],arr[min]=arr[min],arr[i]
    
arr=[64,32,53,21,11]

sel_sort(arr)
print(arr)
