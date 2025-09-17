from brace_simp import brace_simp
from frac_simp import frac_simp

def replace_latex_symbols(input_str: str) -> str:
    correspond = {# 中文标点 -> 英文标点
                  "（": "(", "）": ")", "，": ", ", "．": ".",
                  "。": ". ", "；": "; ", "＂": "\"", "：": ": ", "－": "-",
                  # number fields
                  r"\mathbb{R}": r"\R", r"\boldsymbol{R}" : r"\R", r"\mathbb{Z}": r"\Z",
                  # functions
                  r"\operatorname{Ker}" : r"\ker", r"\operatorname{Im}" : r"\operatorname{im}",
                  r"\operatorname{dim}" : r"\dim", r"\operatorname{ker}" : r"\ker",
                  r"\operatorname{gcd}" : r"\gcd", r"\operatorname{det}" : r"\det",
                  r"\operatorname{deg}": r"\deg",
                  # others
                  r"\mid" : r"|", r"^{\prime}" : r"'", r"\leqslant": r"\le", r"\geqslant": r"\ge",
                  r"\ldots":r"\cdots", r"^{\prime \prime}" : r"''",
                  # arrows
                  r"\Longrightarrow" : r"\implies", r"\Rightarrow" : r"\implies",
                  r"\Longleftrightarrow": r"\iff", r"\rightarrow": r"\to", r"\Leftrightarrow" : r"\iff"}
    for old, new in correspond.items():
        input_str = input_str.replace(old, new)
    return input_str

def main_clean(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line for line in file]
    print(sum(len(line) for line in lines), end = " -> ")
    lines = [replace_latex_symbols(line) for line in lines]
    print(sum(len(line) for line in lines), end = " -> ")

    length_cnt = 0

    for i, line in enumerate(lines):
        line = brace_simp(line)
        lines[i] = frac_simp(line).rstrip()+"\n"
        length_cnt += len(lines[i])

    print(length_cnt)

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
