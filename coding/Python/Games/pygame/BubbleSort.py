import matplotlib.pyplot as plt
import random
import time

def update_plot(arr, title):
    plt.clf()
    plt.bar(range(len(arr)), arr, width=0.5, color='gray')
    plt.title(title)
    plt.xlabel('Index')
    plt.ylabel('Value')

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            update_plot(arr, f'Bubble Sort: Pass {i+1}, Comparison {j+1}')
    return arr

# Generate a scrambled list
scrambled_list = [random.randint(1, 100) for _ in range(20)]

# Initialize the plot
plt.ion()
update_plot(scrambled_list, 'Scrambled List')

# Perform bubble sort and visualize the process
sorted_list = bubble_sort(scrambled_list)

# Final sorted list
update_plot(sorted_list, 'Sorted List')
plt.ioff()
plt.show()