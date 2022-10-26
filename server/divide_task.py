import os
from datetime import datetime
import time

def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]


def divide_task(task_list, sys_count):
    length = len(task_list)
    divide_arr = []
    previous = 0
    curr_sys_id = 1286
    for k in range(sys_count):
        if k == sys_count-1:
            divide_arr.append([previous, length, curr_sys_id])
            break
        divide_arr.append([previous, previous + length//sys_count, curr_sys_id])
        previous = previous + length//sys_count
        curr_sys_id += 1
    file = open("../message/task.txt", "a")
    for division in divide_arr:
        file.write(str(division[0]) + " " + str(division[1]) + " " + str(division[2]) + "\n")
    file.close()
    print("[TASK]: Tasks have been divided.\n")

def handle_divide_task():
    divide_task(numbers, count)

def load_numbers(file_path, array):
    file = open(file_path, "r")
    for line in file.readlines():
        for k in line.split():
            array.append(int(k))
    file.close()



def log_load_operation(start, end, count, file_path):
    file = open(file_path, "a")
    file.write("========================================================================\n")
    file.write("operation: server loading numbers                    {}\n".format(datetime.now()))
    file.write("    loading time: {} seconds\n".format(end-start))
    file.write("    loading items: {}\n".format(count))
    file.write("========================================================================\n")
    file.close()

def log_sort_operation(start, end, count, file_path):
    file = open(file_path, "a")
    file.write("========================================================================\n")
    file.write("operation: server sorting numbers                    {}\n".format(datetime.now()))
    file.write("    sorting time: {} seconds\n".format(end-start))
    file.write("    sorting items: {}\n".format(count))
    file.write("========================================================================\n")
    file.close()




load_start_time = time.process_time()
numbers = []
load_numbers("../sorting/data/numbers.txt", numbers)
load_end_time = time.process_time()
print("Time taken to server load data: {} sec".format(load_end_time - load_start_time))
log_load_operation(load_start_time, load_end_time, len(numbers), "../message/systemlog.txt")

total_sort_start_time = time.process_time()

count = 2
handle_divide_task()


final_sorted_arr = []

def merge_arrays(path1, path2, is_final_empty):
    global final_sorted_arr
    if is_final_empty:
        list1 = []
        list2 = []
        load_numbers(path1, list1)
        load_numbers(path2, list2)
        list1_iter = 0
        list2_iter = 0
        while list1_iter < len(list1) and list2_iter < len(list2):
            if list1[list1_iter] <= list2[list2_iter]:
                final_sorted_arr.append(list1[list1_iter])
                list1_iter += 1
            else:
                final_sorted_arr.append(list2[list2_iter])
                list2_iter += 1
        while list1_iter < len(list1):
            final_sorted_arr.append(list1[list1_iter])
            list1_iter += 1
        while list2_iter < len(list2):
            final_sorted_arr.append(list2[list2_iter])
            list2_iter += 1
    else:
        new_final_arr = []
        list1 = []
        load_numbers(path1, list1)
        list1_iter = 0
        finalarr_iter = 0
        while finalarr_iter < len(final_sorted_arr) and list1_iter < len(list1):
            if list1[list1_iter] <= final_sorted_arr[finalarr_iter]:
                new_final_arr.append(list1[list1_iter])
                list1_iter += 1
            else:
                new_final_arr.append(final_sorted_arr[finalarr_iter])
                finalarr_iter += 1
        while list1_iter < len(list1):
            new_final_arr.append(list1[list1_iter])
            list1_iter += 1
        while finalarr_iter < len(final_sorted_arr):
            new_final_arr.append(final_sorted_arr[finalarr_iter])
            finalarr_iter += 1
        final_sorted_arr = new_final_arr


def get_completed_sys_ids():
    try:
        file = open("../message/sortedlog.txt", "r")
        lines = file.readlines()
        line_values = lines[0].split()
        return_arr = []
        for k in line_values:
            return_arr.append(int(k))
        file.close()
        return return_arr
    except:
        return []

# final_sorted_arr = []
# dir_path = "../helper_sorted/"
dir_path = "../endarrs/"

def handle_merge_arrays():
    final_empty = True
    sorted_files_count = 0
    if count == 1:
        while True:
            # files = os.listdir(dir_path)
            files = list_full_paths(dir_path)
            if len(files) == 1:
                while True:
                    if os.access(files[0], os.X_OK):
                        break
                load_numbers(files[0], final_sorted_arr)
                break
            time.sleep(4)
        return

    while True:
        if final_empty:
            # files = os.listdir(dir_path)
            files = list_full_paths(dir_path)
            if len(files) >= 2:
                # TODO
                completed_sys_ids = get_completed_sys_ids()
                first_sys = int(files[0][-8:-4])
                second_sys = int(files[1][-8:-4])
                while True:
                    if first_sys in completed_sys_ids and second_sys in completed_sys_ids:
                        break
                    time.sleep(5)
                    completed_sys_ids = get_completed_sys_ids()
                # have to check if all helpers have completed writing the sorted array to their respective files.....

                # while True:
                    # if os.access(files[0], os.R_OK) and os.access(files[1], os.R_OK):
                        # break
                merge_arrays(files[0], files[1], True)
                sorted_files_count += 2
                # have to delete the above files
                ################ just for test #########
                # time.sleep(2)
                ########################################
                while True:
                    try:
                        os.remove(files[0])
                        break
                    except:
                        continue
                    # if os.access(files[0], os.X_OK):
                        # os.remove(files[0])
                        # break
                    # time.sleep(2)
                while True:
                    try:
                        os.remove(files[1])
                        break
                    except:
                        continue
                    # if os.access(files[1], os.X_OK):
                        # os.remove(files[1])
                        # break
                    # time.sleep(2)
                # os.remove(files[0])
                # os.remove(files[1])
                final_empty = False
            # else:
                # time.sleep(2)
        else:
            # files = os.listdir(dir_path)
            files = list_full_paths(dir_path)
            if len(files) >= 1:
                while True:
                    if os.access(files[0], os.X_OK):
                        break
                merge_arrays(files[0], "", False)
                sorted_files_count += 1
                # delete above file
                while True:
                    if os.access(files[0], os.X_OK):
                        os.remove(files[0])
                        break
                # os.remove(files[0])
        if sorted_files_count >= count:
            break

handle_merge_arrays()

total_sort_end_time = time.process_time()
print("Time taken to server sort data: {} sec".format(total_sort_end_time - total_sort_start_time))
log_sort_operation(total_sort_start_time, total_sort_end_time, len(final_sorted_arr), "../message/systemlog.txt")


# adding all sorted numbers to a txt file
def store_sorted_arr(arr, file_path):
    file = open(file_path, "w")
    file.write("========================================================================\n")
    file.write("sorted list:                                  {}\n".format(datetime.now()))
    for k in arr:
        file.write(str(k) + " ")
    file.write("\n========================================================================\n")
    file.close()

store_sorted_arr(final_sorted_arr, "../total_sorted_arr.txt")
