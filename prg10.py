list_1=[4,2,-3,1,6]
for i in range(len(list_1)):
    target=0
    temp = []
    for j in range (i+1,len(list_1)):
        target += list_1[j]
        temp.append(list_1[j])
        if(target == 0):
            print(temp)