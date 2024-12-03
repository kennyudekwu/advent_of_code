from heapq import *
from collections import Counter

with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = file_data.split('\n')

def get_first_second_list(input_value):
    first, second = [], []
    for values in input_value:
        first_num, second_num = values.split("   ")
        heappush(first, int(first_num))
        heappush(second, int(second_num))
    return first, second

def main(input_value):
    sim_score = 0
    first, second = get_first_second_list(input_value)
    similarity_map = Counter(first)
    for i in range(len(second)):
        sim_score += similarity_map[second[i]]*second[i]
    return sim_score

def main_(input_value):
    left_list, right_list = get_first_second_list(input_value)
    # Sort both lists
    right_counts = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_counts[num] for num in left_list)
    
    return similarity_score

if __name__ == "__main__":
    print(main(input_value))