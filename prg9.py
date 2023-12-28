arr = [10,20,30,9]
target = 59

for i in range(len(arr)-2):
    for j in range((i+2),len(arr)):
        temp = []
        temp.append(arr[i])
        temp.append(arr[i+1])
        temp.append(arr[j])
        if(target == sum(temp)):
            print(temp)