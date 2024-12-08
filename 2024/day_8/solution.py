from collections import defaultdict

with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = file_data.split('\n')

def main(input_value):
    result = set()
    grid = [list(row) for row in input_value]
    frequencies = defaultdict(list)
    antennas = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != '.':
                frequencies[grid[row][col]].append((row, col))
    for antenna, antennas in frequencies.items():
        anti_node_coords = get_antinodes(0, 1, antennas, grid)
        # print(f"anti-node count for {antenna} is {len(anti_node_coords)}")
        for row, col in anti_node_coords:
            # if (row, col) in result:
            #     print(f"intersection found at ({row}, {col})")
            grid[row][col] = '#' if grid[row][col] == '.' else grid[row][col]
        result.update(anti_node_coords)
    # print(f"antennas not captured: {set([coord for antenna_coords in frequencies.values() for coord in antenna_coords]) - result}")
    # for level in grid:
    #     print(level)
    return len(result)

def get_antinodes(idx, start, antennas, grid):
    row, col = antennas[idx]
    result = set()
    if start < len(antennas):
        for i in range(start, len(antennas)):
            curr_row, curr_col  = antennas[i]
            dy, dx = abs(row-curr_row), col-curr_col
            first_mul = second_mul = 0
            while True:
                first_row, first_col = row-(dy*first_mul), col+(dx*first_mul)
                if not (-1 < first_row < len(grid) and -1 < first_col < len(grid[0])):
                    break
                result.add((first_row, first_col))
                first_mul += 1
            while True:
                second_row, second_col = curr_row+(dy*second_mul), curr_col-(dx*second_mul)
                if not (-1 < second_row < len(grid) and -1 < second_col < len(grid[0])):
                    break
                result.add((second_row, second_col))
                second_mul += 1
                
        valids = get_antinodes(start, start+1, antennas, grid)
        result.update(valids)
    return result


if __name__ == '__main__':
    print(main(input_value))
        
