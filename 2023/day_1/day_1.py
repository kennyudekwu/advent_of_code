import re

with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = file_data.split('\n')


def main():
    def find_num_in_string(string):
        # regex to find all number words in a string overalapping
        result = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', string)
        return result

    total = 0
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for string in input_value:
        nums = find_num_in_string(string)
        digits = set('0123456789')
        if not nums:
            break
        num_1 = numbers.get(nums[0]) if nums[0] not in digits else int(nums[0])
        num_2 = numbers.get(nums[-1]) if nums[-1] not in digits else int(nums[-1])
        total += (int(num_1)*10) + int(num_2)

    return total
if __name__ == "__main__":
    print(main())