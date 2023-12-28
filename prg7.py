non_repeating = [13,31,23,12,32,13,12,3,123,1]


for i in range(len(non_repeating)):
    count = 0
    for j in range((i+1),len(non_repeating)):
        if(non_repeating[i] == non_repeating[j]):
            count =+ 1
    if(count == 0):
        a = non_repeating[i]
        break

print(a)


        