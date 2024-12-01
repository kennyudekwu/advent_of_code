from heapq import heappush, heappop

with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = file_data.split('\n')[1:]

def solution(input_value, start=0):
    total_size , count = 0, 0
    sub_dir_children_total = 0
    sub_dir_children_sizes_list = []
    while start < len(input_value):
        value = input_value[start]
        if value == "$ cd ..":
            break
        if value.startswith("$ cd"):
            sub_dir_count, next_start, sub_dir_total_info = solution(input_value, start+1)
            sub_dir_size, sub_dir_children_size, children_sizes_list = sub_dir_total_info
            heappush(sub_dir_children_sizes_list, sub_dir_size)
            for child_size in children_sizes_list:
                heappush(sub_dir_children_sizes_list, child_size)
            count += sub_dir_count
            total_size += sub_dir_size
            sub_dir_children_total += sub_dir_children_size + (sub_dir_size if sub_dir_size <= 100000 else 0)
            start = next_start
        else:
            value = value.split(' ')
            if value[0].isnumeric():
                total_size += int(value[0])
        start += 1
    count += (total_size <= 100000)
    return (count, start, (total_size, sub_dir_children_total, sub_dir_children_sizes_list))

if __name__ == '__main__':
    count, _, dir_info = solution(input_value)
    dir_total_size, dir_children_total, sub_dir_sizes = dir_info
    result = dir_children_total + (dir_total_size if dir_total_size <= 100000 else 0)
    print("result: ", result)
    print("count: ", count)
    print("dir_total_size: ", dir_total_size)
    unused_space = 70000000 - dir_total_size
    while sub_dir_sizes and unused_space + sub_dir_sizes[0] < 30000000:
        heappop(sub_dir_sizes)
    print("unused_space: ", unused_space)
    print("result: ", sub_dir_sizes[0] if sub_dir_sizes else 0)
    print("space to free up: ", sub_dir_sizes[0])