# two_times.py
def two_times(numberList):
    result = []
    for i in numberList:
        result.append(i*2)
    return result

a = [1,2,3,4]
a = two_times(a)
print(a)
