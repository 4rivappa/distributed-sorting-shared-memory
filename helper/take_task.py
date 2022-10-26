import os
from datetime import datetime
import time

sys_index = 0
start_index = None
end_index = None
sys_id = None

def take_task():
    file = open("../message/task.txt", "r")
    lines = file.readlines()
    values = lines[sys_index].split()
    global start_index
    start_index = int(values[0])
    global end_index
    end_index = int(values[1])
    global sys_id
    sys_id = int(values[2])
    file.close()

def handle_take_task():
    while True:
        # if os.path.getsize("\\\\SIXTYEIGHT\Users\ARIVAPPA\Desktop\dc\message\\task.txt") > 0:
        if os.path.getsize("../message/task.txt") > 1:
            take_task()
            break
        time.sleep(6)

def load_numbers(file_path, array):
    file = open(file_path, "r")
    for line in file.readlines():
        for k in line.split():
            array.append(int(k))
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

def store_sorted_arr(arr, file_path):
    file = open(file_path, "a")
    for k in arr:
        file.write(str(k) + " ")
    file.close()


def log_load_operation(start, end, count, file_path):
    file = open(file_path, "a")
    file.write("========================================================================\n")
    file.write("operation: {} loading numbers                    {}\n".format(sys_id, datetime.now()))
    file.write("    loading time: {} seconds\n".format(end-start))
    file.write("    loading items: {}\n".format(count))
    file.write("========================================================================\n")
    file.close()

def log_sort_operation(start, end, count, file_path):
    file = open(file_path, "a")
    file.write("========================================================================\n")
    file.write("operation: {} sorting numbers                    {}\n".format(sys_id, datetime.now()))
    file.write("    sorting time: {} seconds\n".format(end-start))
    file.write("    sorting items: {}\n".format(count))
    file.write("========================================================================\n")
    file.close()


handle_take_task()

numbers = []
load_start_time = time.process_time()
load_numbers("../sorting/data/numbers.txt", numbers)
load_end_time = time.process_time()

print("Time taken to load data: {} seconds".format(load_end_time - load_start_time))
log_load_operation(load_start_time, load_end_time, len(numbers), "../message/system" + str(sys_id) + "log.txt")

# handle_take_task()

curr_numbers = numbers[start_index : end_index]
sort_start_time = time.process_time()
merge_sort(curr_numbers)
sort_end_time = time.process_time()

print("Time taken to sort data: {} seconds".format(sort_end_time - sort_start_time))
log_sort_operation(sort_start_time, sort_end_time, len(curr_numbers), "../message/system" + str(sys_id) + "log.txt")


store_sorted_arr(curr_numbers, "../endarrs/"+str(sys_id)+".txt")


def enter_sortedlog(system_id):
    file = open("../message/sortedlog.txt", "a")
    file.write(str(system_id) + " ")
    file.close()

enter_sortedlog(sys_id)


print("[Finished]: successfully sorted given array...!\n")

