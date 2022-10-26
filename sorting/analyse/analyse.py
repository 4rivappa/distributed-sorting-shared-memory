import time
from datetime import datetime

def load_numbers(file_path, array):
    file = open(file_path, "r")
    for line in file.readlines():
        for k in line.split():
            array.append(int(k))
    file.close()

def log_load_operation(start, end, count, file_path):
    file = open(file_path, "a")
    file.write("========================================================================\n")
    file.write("operation: loading numbers                    {}\n".format(datetime.now()))
    file.write("    loading time: {} seconds\n".format(end-start))
    file.write("    loading items: {}\n".format(count))
    file.write("========================================================================\n")
    file.close()

def log_sort_operation(start, end, count, file_path):
    file = open(file_path, "a")
    file.write("========================================================================\n")
    file.write("operation: sorting numbers                    {}\n".format(datetime.now()))
    file.write("    sorting time: {} seconds\n".format(end-start))
    file.write("    sorting items: {}\n".format(count))
    file.write("========================================================================\n")
    file.close()

def store_sorted_arr(arr, file_path):
    file = open(file_path, "a")
    file.write("========================================================================\n")
    file.write("sorted list:                                  {}\n".format(datetime.now()))
    for k in arr:
        file.write(str(k) + " ")
    file.write("\n========================================================================\n")
    file.close()

def merge_sort(array):
    if len(array) <= 1:
        return
    mid_point = len(array)//2
    left_arr = array[:mid_point]
    right_arr = array[mid_point:]
    merge_sort(left_arr)
    merge_sort(right_arr)
    left_iter = right_iter = arr_iter = 0
    while left_iter < len(left_arr) and right_iter < len(right_arr):
        if left_arr[left_iter] < right_arr[right_iter]:
            array[arr_iter] = left_arr[left_iter]
            left_iter += 1
        else:
            array[arr_iter] = right_arr[right_iter]
            right_iter += 1
        arr_iter += 1
    while left_iter < len(left_arr):
        array[arr_iter] = left_arr[left_iter]
        left_iter += 1
        arr_iter += 1
    while right_iter < len(right_arr):
        array[arr_iter] = right_arr[right_iter]
        right_iter += 1
        arr_iter += 1

numbers = []

load_start_time = time.process_time()
load_numbers("../data/numbers.txt", numbers)
load_end_time = time.process_time()

print("Time taken to load data: {} sec".format(load_end_time - load_start_time))
log_load_operation(load_start_time, load_end_time, len(numbers), "log_file.txt")

sort_start_time = time.process_time()
merge_sort(numbers)
sort_end_time = time.process_time()

print("Time taken to sort data: {} sec".format(sort_end_time - sort_start_time))
log_sort_operation(sort_start_time, sort_end_time, len(numbers), "log_file.txt")

store_sorted_arr(numbers, "sorted_list.txt")

del numbers
