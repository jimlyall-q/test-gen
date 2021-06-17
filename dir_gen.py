#!/usr/bin/env python
from sys import stdin
from os import mkdir, makedirs, chdir

ts_template = """
from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestSuite


"""


template = """
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
"""
setup = """
    async def setup(self) -> None:
        logger.info("No setup")
"""

execute = """
    async def execute(self) -> None:
"""

cleanup = """
    async def cleanup(self) -> None:
        logger.info("No cleanup")
"""

# TODO this should also have the TestSuiteID or the TestCaseID
metadata_template = """
    metadata = {
        "public_id": "{metadata_public_id}",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

"""

metadata_template1 = """
    metadata = {
        "public_id": """
metadata_template2 = """",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

"""


# we need a folder a test and an __init__.py for each case
def populate_dirs(tcs, dir='topdir'):
    mkdir(dir)
    chdir(dir)
    with open('__init__.py', 'a') as package_init:
        package_init.write('from .' + dir + ' import ' +
                           dir.upper().replace('_', '') + 'TestSuite' + '\n')
    with open(dir + '.py', 'a') as ts_init:
        ts_init.write(ts_template)
        ts_init.write('class ' + dir.upper().replace('_', '') +
                      "TestSuite(TestSuite):")
        ts_init.write(metadata_template1 + '"' +
                      dir.upper().replace('_', '') + 'TestSuite' + metadata_template2)

        ts_init.write(setup)
        ts_init.write(cleanup)

    for test in tcs:
        dir_name = test['test_name'].replace('-', '').replace('.', '_')
        assert(test['test_num'])
        assert(test['test_name'])
        assert(test['test_title'])
        print(test['test_num'])
        print(test['test_name'])
        print(test['test_title'])
        mkdir(dir_name)
        chdir(dir_name)
        with open('__init__.py', 'a') as package_init:
            package_init.write('from .' + dir_name.lower() +
                               ' import ' + dir_name + '\n')

        with open(dir_name.lower() + '.py', 'a') as class_file:
            class_file.write(template)
            class_file.write('class ' + dir_name + "(TestCase):\n")
            dir_name
            class_file.write(metadata_template1 + '"' +
                             dir_name + metadata_template2)
            class_file.write(setup)
            class_file.write(execute)
            class_file.write(cleanup)

        chdir('..')


count = 1
posn = 0

cols = ['test_num', 'test_name', 'test_title']

tcs = []
foodict = {}


line = stdin.readline()
while line:
    line = line.strip()
    if line.strip() == "":
        line = stdin.readline()
        continue

    if line.isdigit():
        # and (posn == 4 or posn == 0):  # should be test step for goods
        if (count != 1):
            # print(foodict)
            tcs.append(foodict)
        foodict = {}
        posn = 0
        print(line, count)
        assert(int(line) == count)
        count += 1
        foodict[cols[posn]] = int(line)
    else:
        posn += 1
        foodict[cols[posn]] = line

    line = stdin.readline()
    if not line:
        tcs.append(foodict)

populate_dirs(tcs, dir='tcsc')

if __name__ == '__main__':
    print('fnished')
