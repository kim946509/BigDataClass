import random
import matplotlib.pyplot as plt


a = []
b = []
first = 0
second = 0
total = 0
total_try = 1000000

# for k in range(1, total_try):
#     i = random.randint(1, 6)
#     j = random.randint(1, 6)
#     if (i == 3 and j == 3):
#         total += 1
# print(total/total_try)

# for k in range(1, total_try):
#     i = random.randint(1, 6)
#     if(i == 3):
#         first = first+1
#         j = random.randint(1, 6)
#         if(j == 3):
#             second = second+1
# print(second/first)

for k in range(1, total_try):
    i = random.randint(1, 6)
    j = random.randint(1, 6)
    if(j == 3):
        second = second+1
print(second/total_try)
