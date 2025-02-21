import time

s = input()

start_time = time.time()

if s[0] == "\"":
    s = s[1 : -1]

filename = "C:\\Users\\yuany\\Desktop\\Markdown\\format_input.md" if len(s) == 1 else s

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    pos = [i for i, line in enumerate(lines) if line == "$$\n"]

    # 生成配对，确保偶数个$$
    if len(pos) % 2 != 0:
        print("警告：存在未闭合的$$公式块，最后一组将被忽略。")
    pair = list(zip(pos[::2], pos[1::2]))

    for start, end in pair:
        if end - start == 2:
            lines[start] = "\0"
            lines[start + 1] = f"${lines[start + 1].strip()}$\n"
            lines[end] = "\0"

    output_path = "C:\\Users\\yuany\\Desktop\\Markdown\\format_output.txt"
    with open(output_path, "w", encoding="utf-8") as file:
        file.writelines(line for line in lines if line != "\0")

except FileNotFoundError:
    print(f"错误：文件 {filename} 未找到。")
except Exception as e:
    print(f"发生未知错误：{e}")

end_time = time.time()
print(f"代码运行时间：{end_time - start_time} 秒")