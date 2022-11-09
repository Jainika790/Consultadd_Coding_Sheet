def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            
if __name__ == '__main__':
    arr = [4,1,3,9,8,7]
    bubbleSort(arr)
    print(arr)