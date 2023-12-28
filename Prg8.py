arr = [43,31,23,12,32,13,12,3,123,1]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr[0])
