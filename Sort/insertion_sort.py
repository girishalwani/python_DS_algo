def insertion_sort(arr):
    for i in range(0,len(arr)):
        key=arr[i]
        
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    
    return arr


arr=[64,12,46,42,11,23]
sort=insertion_sort(arr)

print(sort)
