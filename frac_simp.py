import re

from brace_simp import greek_letters_with_slash

def frac_pos(line_s: str) -> list:
    return [match.start() for match in re.finditer(r"frac", line_s)]

def is_num(s : str):
    return len(s) == 1 and s.isdigit()

def frac_simp(line_s : str, brace_pair : dict) -> str:
    line = list(line_s)
    for index in frac_pos(line_s):
        start, end = index + 4, -1
        content1 = ""
        if start in brace_pair:
            end = brace_pair[start]
            content1 = line_s[start + 1: end]

            if is_num(content1):
                line[start], line[end] = "\0", "\0"
            elif content1 in greek_letters_with_slash:
                line[start], line[end] = "\0", "\0" if line[end + 1] == r"{" or "\\" or " " else " "

        elif line[start].isdigit():
            end = start
            content1 = line[start]
        else: continue

        start = end + 1
        if start not in brace_pair: continue
        end = brace_pair[start]
        content2 = line_s[start + 1: end]

        valid_cond = ( (is_num(content1) and len(content2) == 1)
                        or (content2 in greek_letters_with_slash)
                        or is_num(content2) )

        if valid_cond:
            line[start], line[end] = "\0", "\0" if line[end + 1] == " " else " "
    return "".join(c for c in line if c != "\0")