with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = file_data.split('\n')

def main(input_value):
    start_x, start_y = None, None
    direction = {
        "^": [(-1,0), (0,1), ">"],
        ">": [(0,1), (1,0), "v"],
        "<": [(0,-1), (-1,0), "^"],
        "v": [(1,0), (0,-1), "<"]
    }
    grid = []
    for i in range(len(input_value)):
        current_level = []
        for j in range(len(input_value[i])):
            if input_value[i][j] in direction:
                start_x, start_y = i, j
            current_level.append(input_value[i][j])
        grid.append(current_level)
    patrol_area = traverse(grid, start_x, start_y, grid[start_x][start_y], direction)
    patrol_area.remove((start_x, start_y))
    return obstacle_count(grid, patrol_area, grid[start_x][start_y], direction, start_x, start_y)

def obstacle_count(grid, patrol_area, orientation, direction, start_x, start_y):
    obstacle_count = 0
    for row, col in patrol_area:
        temp = grid[row][col]
        grid[row][col] = "#"
        obstacle_count += bool(can_contain_guard(grid, start_x, start_y, orientation, direction))
        grid[row][col] = temp
    return obstacle_count

def can_contain_guard(grid, row, col, orientation, direction):
    # Iterative Simple DFS
    # seen = set()
    # while -1 < row < len(grid) and -1 < col < len(grid[0]):
    #     if (row, col, orientation) not in seen:
    #         seen.add((row, col, orientation)) # take note of travel direction as paths can be visited again, coming from a different direction
    #     else:
    #         return True
    #     row, col, orientation = walk(grid, row, col, orientation, direction)
    # return False

    # FLoyd's Cycle Detection
    slow_row, slow_col, slow_orientation = row, col, orientation
    fast_row, fast_col, fast_orientation = walk(grid, slow_row, slow_col, orientation, direction)
    while (slow_row, slow_col, slow_orientation) != (fast_row, fast_col, fast_orientation):
        slow_row, slow_col, slow_orientation = walk(grid, slow_row, slow_col, slow_orientation, direction)
        fast_row, fast_col, fast_orientation = walk(grid, fast_row, fast_col, fast_orientation, direction)
        fast_row, fast_col, fast_orientation = walk(grid, fast_row, fast_col, fast_orientation, direction)
        if not (-1 < fast_row < len(grid) and -1 < fast_col < len(grid[0])):
            return False
    return True


def traverse(grid, row, col, orientation, direction):
    seen = set()
    while -1 < row < len(grid) and -1 < col < len(grid[0]):
        if grid[row][col] != "#":
            seen.add((row, col))
        row, col, orientation = walk(grid, row, col, orientation, direction)
    return seen

def walk(grid, row, col, orientation, direction):
    if not (-1 < row < len(grid) and -1 < col < len(grid[0])):
        return row, col, orientation
    if grid[row][col] == "#":
            prev_row, prev_col = row-direction[orientation][0][0], col-direction[orientation][0][1]
            row, col = prev_row+direction[orientation][1][0], prev_col+direction[orientation][1][1]
            orientation = direction[orientation][2]
    else:
        row, col = row+direction[orientation][0][0], col+direction[orientation][0][1]
    return row, col, orientation

if __name__ == '__main__':
    print(main(input_value))
        
