#!/usr/bin/env python
"creates a new python file and updates readme"

import sys
from pathlib import Path


def create_file(name):
    num = list(name[0])

    if num[-1] == ".":
        num.pop()

    num.insert(0, "0" * (4 - len(num)))
    num = "".join(num)

    assert len(num) == 4, "file number should be 4 characters"

    for word in name[1:]:
        word.capitalize()

    file_name = num + "_" + "".join(name[1:]) + ".py"

    Path(f"./python/{file_name}").touch()

    return num


def get_number(line):
    if line and line[3:7].isdigit():
        return int(line[3:7])
    return -1


def update_readme(num, name):

    url = (
        "https://leetcode.com/problems/"
        + "-".join(map(lambda x: x.lower(), name[1:]))
        + "/"
    )

    new_line = f"|[{num}. {''.join(name[1:])}]({url})|x|||\n"

    with open("README.md") as fp:
        lines = fp.readlines()

    prev = -1
    for i, line in enumerate(lines):
        cur = get_number(line)
        if int(num) > cur:
            prev = i
        else:
            lines.insert(prev, new_line)
            break

    with open("README.md", "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    name = sys.argv[1:]
    num = create_file(name)
    update_readme(num, name)
