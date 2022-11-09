def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(min_index+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        
        if i!= min_index:
            arr[i],arr[min_index] = arr[min_index],arr[i]

if __name__ == '__main__':
    elements=[4,1,3,9,7]
    selection_sort(elements)
    print(elements)