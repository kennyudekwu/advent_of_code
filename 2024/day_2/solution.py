with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = file_data.split('\n')

def main(input_value, correctable=1):
    count = 0
    for values in input_value:
        values = values.split()

        # Linear time complexity
        count += bool(traverse(values) or traverse(values, asc=False))

        # DP - recursive memoized solution - exponential time complexity
        # if is_safe(values) or is_safe(values, asc=False):
        #     count += 1
        # else:
        #     count += bool(can_be_safe(values, correctable, {}))
        
    return count

def is_safe(values, asc=True):
    for i in range(1, len(values)):
        prev, curr = int(values[i-1]), int(values[i])
        if abs(prev - curr) > 3 or (asc and prev > curr) or (not asc and prev < curr):
            return False
    return True

def can_be_safe(values, correctable, verdict_map):
    values = tuple(values)
    if values in verdict_map:
        return verdict_map[values]
    verdict_map[values] = is_safe(values) or is_safe(values, asc=False)
    if not verdict_map[values] and correctable > 0:
        for i in range(len(values)):
            verdict_map[values] = can_be_safe(values[:i] + values[i+1:], correctable-1, verdict_map)
            if verdict_map[values]:
                break
    return verdict_map[values]

def traverse(values, asc=True):
    bad_forward = corrections(values, asc)
    if bad_forward > 1:
        return corrections(values, asc, forward=False) < 2
    return True

def corrections(values, asc, forward=True):
    bad = 0
    start, stop, step = 1, len(values), 1
    if not forward:
        start, stop, step = stop-2, -1, -1
    i = start
    prev = int(values[start-step])
    while i != stop:
        curr = int(values[i])
        current_diff = prev-curr if asc else curr-prev
        if not (1<=current_diff<=3):
            bad += 1
            if bad > 1:
                break
        else:
            prev = curr
        i += step
    return bad

if __name__ == "__main__":
    print(main(input_value))   