with open("./input.txt", "r") as file:
    equations = []
    for line in file:
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))

def main(equations):
    total_calibration_result = 0
    for target, numbers in equations:
        valid = possible(numbers, 0, len(numbers), 0, target, 0)
        if valid:
            total_calibration_result += target
    return total_calibration_result

def possible(num, start, end, i, target, current_val):
    if not num:
        return False
    if i > len(num)-1:
        return target == current_val
    if current_val > target:
        return False
    return possible(num, start, end, i+1, target, current_val+num[i]) or possible(num, start, end, i+1, target, current_val*num[i]) or possible(num, start, end, i+1, target, int(str(current_val)+str(num[i])))

if __name__ == "__main__":
    print(main(equations))
        
