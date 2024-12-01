import timeit
import cProfile

# pre-processing

# generate input map
with open('new_input.txt', 'r') as file:
    file_data = file.read()
    chunks = file_data.split('\n\n')

input_map = {}
input_list = chunks[0][7:].split() # input list - list of seeds
chunks = chunks[1:]

for chunk in chunks:
    chunk = chunk.split('\n')
    chunk = [x for x in chunk if x]
    chunk_list = []
    for i in range(1, len(chunk)):
        line = chunk[i]
        line = line.split()
        source_start, dest_start, step = int(line[1]), int(line[0]), int(line[2])-1
        source_end, dest_end = source_start+step, dest_start+step
        chunk_list.append([(source_start, source_end), (dest_start, dest_end)])
    input_map[chunk[0].split('-')[0]] = chunk_list

# main function
def main(input_list, input_map):
    # list containing literal source names - always constant
    source_list = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature',
                   'humidity'] # location is not a destination hence its absence
    return traverse(merge_ranges(input_list), source_list, 0, input_map)

'''
Algorithm:
- convert map to array of arrays of tuples -> map = [[(source_start, source_end), (dest_start, dest_end)]]
- sort, map by start of ranges as you go - do this for every level
- merge overlapping input seed ranges
- loop through seed ranges
- for each seed range - find the intersection between the range and the source ranges
- churn out intersection between input range and a map range - return intersecting ranges and non-intersecting ranges
- for intersecting range, append to list and for non-intersecting, use post ranges to compare to next range in input map
- for intersecting ranges, return destination range while for non-intersecting, return just range
- use the resulting newly spawned non-intersecting ranges to spawn more ranges by going through rest of source ranges in current map
- procedure continues till end of the map
- result will be the first number of the first range
'''

def merge_ranges(input_list):
    input_list = [(int(input_list[i]), int(input_list[i])+(int(input_list[i+1])-1)) for i in range(0, len(input_list), 2)]
    input_list.sort()
    merged = [input_list[0]]
    for i in range(1, len(input_list)):
        start, end = input_list[i]
        if merged[-1][1] >= start:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append(input_list[i])
    return merged

def traverse(input_ranges, source_list, source_idx, input_map):
    if source_idx == len(source_list):
        return sorted(input_ranges)[0][0]
    target_ranges = input_map[source_list[source_idx]]
    target_ranges.sort()
    ranges = set()
    for input_range in input_ranges:
        intersects = compute_intersects(input_range, target_ranges)
        ranges = ranges.union(intersects)
    return traverse(ranges, source_list, source_idx+1, input_map)  

def compute_intersects(input_range, target_ranges):
    result = set()
    for target_range in target_ranges:
        if not input_range:
            break
        input_start, input_end = input_range
        target_start_source, target_end_source = target_range[0]
        
        if not input_end <= target_start_source and not input_start >= target_end_source:
            if (target_start_source <= input_start <= target_end_source) or (target_start_source <= input_end <= target_end_source):
                intersect = (max(input_start, target_start_source), min(input_end, target_end_source))
                result.add(get_dest_equivalent(target_range[0], intersect, target_range[1]))
            if target_start_source >= input_start and target_end_source <= input_end:
                result.add(target_range[1])
            if input_start < target_start_source:
                result.add((input_start, target_start_source-1))
            if target_end_source < input_end:
                input_range = (target_end_source+1, input_end)
            else:
                input_range = None
        elif input_end <= target_start_source:
            result.add(input_range)
            input_range = None
            break
    if input_range:
        result.add(input_range)

    return result

def get_dest_equivalent(source_range, intersect_range, dest_range):
    step = intersect_range[0] - source_range[0]
    intersect_range_length  = intersect_range[1] - intersect_range[0]
    new_range = (dest_range[0] + step, dest_range[0] + step + intersect_range_length)
    return new_range

def run():
    print(main(input_list, input_map))

def time():
    s = timeit.default_timer()
    for _ in range(100):
        main(input_list, input_map)
    e = timeit.default_timer() - s
    print(e)
    print(e/100)

def profile():
    cProfile.run('time()')

time()
