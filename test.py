# def frac_simp(line_s : str, brace_pair : dict) -> str:
#     line = list(line_s)
#     for index in frac_pos(line_s):
#         start = index + 4
#         # end = brace_pair[start] if start in brace_pair else None
#         # if not end : continue
#         # top = line_s[start + 1: end]
#         #
#         # start = end + 1
#         # end = brace_pair[start] if start in brace_pair else None
#         # if not end: continue
#         # top = line_s[start + 1: end]
#         # pass
#
# def isvalid_frac_simp(top : str, bot : str) -> (bool, bool):
#     ans = [False, False] # F 表示不脱括号, T 表示脱括号
#     if len(top) == 1 and top[0].isdigit():
#         ans[0] = True
#         if
#     if top in greek_letters_with_slash:
#         ans[0] = True
#         if bot in greek_letters_with_slash or\
#             len(bot) == 1 and bot[0].isdigit():
#             ans[1] = True
#
#     pass
# (line, x, y, i) -> bool:
#     return "".join(line[x + 1:y]) in  or \
#         (y - x == 2 and (1 if i == 1 else line[x + 1].isdigit()))
#     # 0表示分子, 1表示分母
