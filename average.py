#lists in for loop
total=0;
numbers=[10,20,30,40,50,60]
for num in numbers:
    total=total+num;
average=total/len(numbers)
print ("The average of {} is {}".format(numbers,average))
