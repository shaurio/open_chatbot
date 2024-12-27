
import statistics
print("hello")


my_list = [1,2,3,4,5,6,7,8,9]

def mean(my_list):
    total = 0
    for i in my_list:
        total = total + i
    return total / len(my_list)

print(mean(my_list))

print(statistics.stdev(my_list))
