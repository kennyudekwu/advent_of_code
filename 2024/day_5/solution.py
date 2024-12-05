from collections import defaultdict, deque
from functools import partial

with open('./input.txt', 'r') as file:
    file_data = file.read()
    page_order_value = file_data.split('\n')

with open('./updates.txt', 'r') as update_file:
    update_data = update_file.read()
    updates = update_data.split('\n')
        
def top_sort(update, rules):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    for before, after in rules:
        if before in update and after in update: 
            graph[before].add(after)
            in_degree[after] += 1
            in_degree[before] += 0

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_order

def main(page_order_value, updates):
    final = 0
    rules = [line.split('|') for line in page_order_value]
    for update in updates:
        update = update.split(',')
        ordered = top_sort(update, rules)
        if ordered != update:
            final += int(ordered[len(update)//2])
    return final

if __name__ == '__main__':
    print(main(page_order_value, updates))