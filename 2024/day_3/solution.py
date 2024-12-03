import re

with open('./input.txt', 'r') as file:
    file_data = file.read()

def main(input_value):
    sm = 0
    main_pattern = r"mul\((\d+),(\d+)\)"
    for value in input_value:
        matches = get_match(value)
        for i in range(len(matches)):
            if i == 0:
                result = re.findall(main_pattern, matches[i])
                for num1, num2 in result:
                    sm += int(num1) * int(num2)
            else:
                _, _, match = matches[i].partition("do")
                if match:
                    result = re.findall(main_pattern, match)
                    for n1, n2 in result:
                        sm += int(n1) * int(n2)
    return sm

def get_match(string):
    matches = string.split("don't")
    return matches

if __name__ == '__main__':
    print(main([file_data]))
        
