from brace_simp import greek_letters_with_slash

def frac_pos(char_list: list[str]) -> list[int]:
    res = []
    for i in range(len(char_list) - 3):
        if char_list[i:i + 4] == ['f', 'r', 'a', 'c']:
            res.append(i)
    return res

def is_num(s : list):
    return len(s) == 1 and s[0].isdigit()

def frac_simp(line : list[str], brace_pair : dict) -> str:
    for index in frac_pos(line):
        start, end = index + 4, -1
        if start in brace_pair:
            end = brace_pair[start]
            content1 = line[start + 1: end]
            if is_num(content1):
                line[start], line[end] = "\0", "\0"
            elif "".join(content1) in greek_letters_with_slash:
                line[start] = "\0"
                line[end] = "\0" if line[end + 1] in {"{", "\\", " ", r"}", ")", "(", "$"} else " "

        elif line[start].isdigit():
            end = start
            content1 = line[start]
        else: continue

        start = end + 1
        if start not in brace_pair: continue
        end = brace_pair[start]
        content2 = line[start + 1: end]

        valid_cond = ( (is_num(content1) and len(content2) == 1)
                        or ("".join(content2) in greek_letters_with_slash)
                        or is_num(content2) )

        if valid_cond:
            line[start] = "\0"
            line[end] = "\0" if line[end + 1] in {"{", "\\", " ", r"}", ")", "(", "$"} else " "

    return "".join(c for c in line if c != "\0")