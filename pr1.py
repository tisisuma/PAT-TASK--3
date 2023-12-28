list_1=[10,501,22,37,100,999,87,351]
ev_li = []
od_li = []
for i in list_1:
        if (i % 2 == 0):
            ev_li.append(i)
        else:
            od_li.append(i)
print("Even lists:", ev_li)
print("Odd lists:", od_li)
 
 