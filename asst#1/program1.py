import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print("sorted ages :",sorted(ages)) #sorted list
print("Max age is :",max(ages))
print("Min age is :",min(ages))
#adding min and max numbers to the ages list
ages.append(min(ages))
ages.append(max(ages))
print("after adding min and max ages :",ages)

#median of the ages list
print("median : ",statistics.median(ages))

#average of the ages list.
print("average :",sum(ages)/len(ages))

#range of the list
print("range of ages :",max(ages)-min(ages))
