import math
def avg(list):
    return sum(list)/len(list) 

def sumSqDiff(list,av):
    return sum((x-av)**2 for x in list)

numbers = [1,12,3,31,5,7]
average=avg(numbers)
ssd = sumSqDiff(numbers,average)

standardDeviation = math.sqrt(ssd/len(numbers))

print("Numbers:  ",numbers)
print("Average:  ",average)
print("Sum of squared differences",ssd)
print ("Standard Deviation:  ",standardDeviation)





