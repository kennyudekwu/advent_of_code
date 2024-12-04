with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = file_data.split('\n')

def main(grid):
    result = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for row_direction, col_direction in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                word = count(grid, row, col, row_direction, col_direction, "XMAS", 0)
                if word:
                    result.append(word)
    return len(result)

def count(grid, row, col, row_direction, col_direction, word, i):
    curr_row, curr_col = row+(row_direction*i), col+(col_direction*i)
    if not (-1 < curr_row < len(grid)) or not (-1 < curr_col < len(grid[0])) or grid[curr_row][curr_col] != word[i]:
        return []
    if i == len(word) - 1:
        return [(curr_row, curr_col)]
    coords = count(grid, row, col, row_direction, col_direction, word, i+1)
    return [(curr_row, curr_col)] + coords if coords else []

if __name__ == '__main__':
    grid = [list(line) for line in input_value]
    print(main(grid))
