import random
L = [random.random() for i in range(100000)]
print("sorting an unsorted list:")
%time L.sort()
