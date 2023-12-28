# Given number list
numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12]
 
# Empty list
primelist = []
 
# Iterate through each number form the list
for num in numberList :
     
    # 0 and 1 is not a prime number so skip this number
    if num == 0 or num == 1 :
        continue
         
    # loop from 2 to half of the given number
    for i in range(2, num // 2 + 1) :
 
        # If number is divisible by any number (i) then it is not a prime number
        if num % i == 0 :
            break
 
    # If not divisible then it is a prime number
    else :
         
        # if number is prime
        # then append to the list
        primelist.append(num)
print("Number of prime number in the list",len(primelist))
print(primelist)
