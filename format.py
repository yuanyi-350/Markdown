import time

from brace_simp import brace_simp, brace_pair_pos
from frac_simp import frac_simp

correspond = {"（": "(",  "）": ")",
              "，": ", ",  "．": ". ",
              "。": ". ",  "；": "; ",
              "＂": "\"",  "：": ": "}#中文标点 -> 英文标点

s = input()

start_time = time.time()

if s[0] == "\"": s = s[1 : -1]
filename = "C:\\Users\\yuany\\Desktop\\Markdown\\format_input.md" if len(s) == 1 else s
with open(filename, "r", encoding="utf-8") as file:
    lines = [line for line in file]

before_cnt, now_cnt = 0, 0

for i in range(len(lines)):
    new_line1 = []
    for c in lines[i]:
        new_line1.append(correspond.get(c, c))
    before_cnt += len(new_line1)

    brace_pair = brace_pair_pos(new_line1)
    new_line2 = brace_simp(new_line1, brace_pair)
    lines[i] = frac_simp(new_line2, brace_pair)

    now_cnt += len(lines[i])

with open("C:\\Users\\yuany\\Desktop\\Markdown\\format_output.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line.rstrip()+"\n")

print(f"{now_cnt} / {before_cnt}")

end_time = time.time()
print(f"代码运行时间：{end_time - start_time} 秒")