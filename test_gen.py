#!/usr/bin/env python
from sys import stdin
import re

# Put the words in the test case/steps
def populate_tc(steps):
    print("    def create_test_steps(self) -> None:")
    print('        self.test_steps = [')
    for step in steps:
        print('            TestStep("Test Step ' + step['test_id'] + ': ' + step['test_title']+ '"),')
    print('    ]')
    for step in steps:
        print('\n        # ' + step['test_id'] + ': ' + step['test_title'])
        for test in step['test_desc'].split('.'):
            print('        # ' + test.strip())

        print('        logger.info("' + step['test_id'] + ': ' + step['test_title'] + '")')
        print('        self.next_step()')

def getnextline_on_stdin():
    lines = stdin.readlines()
    print(lines)
    for line in lines:
        line = line.strip()
        while line == "":
            print('reading')
            return
        else:
            print(line)
            yield line

    return        
    # line = stdin.readline()


count = 1
posn = 0

cols = ['step_num', 'test_id', 'test_title', 'test_desc']

steps = []
foodict = {}

line = stdin.readline()
while line:
    is_new_entry = False
    line = line.strip()
    if line.strip() == "":
        line = stdin.readline()
        continue

    matched = re.search('^(\d+)(\.)?([abcdefghijklmnopqrstuvwxyz])?', line)
    if matched:
        is_new_entry = (matched.group(1) is not None) and ((matched.group(2) is not None) ==
                                             (matched.group(3) is not None))
        # print((matched.group(1)), (matched.group(2)), (matched.group(3)))
        # print(matched.groups(), len(matched.groups()), (matched.group(2) is not None) == (matched.group(3) is not None))

    # print(line)
    if is_new_entry:
        if (count != 1):
            print(foodict)
            steps.append(foodict)
        foodict = {}
        posn = 0
        # print(line, count)
        # assert(int(line) == count)
        count += 1
        foodict[cols[posn]] = line
    elif line[0:1] == 'IF':
        print('foundif')
        foodict['conditional'] = line
    else:
        posn += 1
        if posn >= len(cols):
            foodict[cols[len(cols)-1]] = foodict[cols[len(cols)-1]] + '.' + line
        else:
            foodict[cols[posn]] = line
        # print(posn, line)

    line = stdin.readline()
    if not line:
        # pass
        # print("line")
        print(foodict)
        steps.append(foodict)

    
populate_tc(steps)

if __name__ == '__main__':
    print('shebango')