def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr

arr=[64,12,46,42,11,23]

sorted=bubble_sort(arr)

print(sorted)
