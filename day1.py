import regex as re

first_num = 0
last_num = 0
sums = []

wordToNum = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def findWordNums(line):
    regex = '(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9)'
    return re.findall(regex, line, overlapped=True)

with open('exampleInput.txt') as text_file:
    file1 = text_file.readlines()

    for line in file1:
        nums = findWordNums(line)
        first_num = nums[0]
        last_num = nums[-1]

        if first_num in wordToNum:
            first_num = wordToNum[first_num]
        if last_num in wordToNum:
            last_num = wordToNum[last_num]

        sums.append(f'{first_num}' + f'{last_num}')

    total = 0
    for str in sums:
        total += int(str)

    print(total)
