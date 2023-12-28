list_1=[10,20,30,40,50]
list_2=[20,40,60,80,100]
list_3=[30,60,90,120,150]
temp=[]
for i in list_2:
   list_1.append(i)
print(list_1)

for j in list_3:
   list_1.append(j)
print(list_1)

for k in list_1:
   if k not in temp:
      temp.append(k)
print(temp)