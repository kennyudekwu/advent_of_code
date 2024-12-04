with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = file_data.split('\n')

def main(grid):
    result = 0
    for row in range(1,len(grid) - 1):
        for col in range(1,len(grid[0]) - 1):
            if grid[row][col] == "A":
                sub_grid = [[grid[r][c] for c in range(col-1, col+2)] for r in range(row-1, row+2)]
                sub_grid[1][0], sub_grid[1][2], sub_grid[0][1], sub_grid[2][1] = ".", ".", ".", "."
                # result += bool(valid(grid, row, col))
                result += valid_xmas_pattern(sub_grid)
    return result

def valid_xmas_pattern(subgrid):
    valid_patterns = [
        [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]],
        [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]],
        [["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]],
        [["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]],
    ]
    return subgrid in valid_patterns
    # for pattern in valid_patterns:
    #     if matches_pattern(subgrid, pattern):
    #         return 1
    # return 0


def valid(grid, row, col):
    if grid[row-1][col-1] == "M" and grid[row+1][col+1] == "S" and grid[row+1][col-1] == "M" and grid[row-1][col+1] == "S":
        return True
    if grid[row-1][col-1] == "M" and grid[row+1][col+1] == "S" and grid[row+1][col-1] == "S" and grid[row-1][col+1] == "M":
        return True
    if grid[row-1][col-1] == "S" and grid[row+1][col+1] == "M" and grid[row+1][col-1] == "M" and grid[row-1][col+1] == "S":
        return True
    if grid[row-1][col-1] == "S" and grid[row+1][col+1] == "M" and grid[row+1][col-1] == "S" and grid[row-1][col+1] == "M":
        return True
    return False
    

if __name__ == '__main__':  
    grid = [list(row) for row in input_value]

    print(main(grid))  # Output the number of X-MAS occurrences