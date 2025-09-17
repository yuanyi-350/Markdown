import re
from brace_simp import escaped_greek

pattern = r"\{(\d|" + escaped_greek + r")\}"

def frac_simp(line : str) -> str:
    line = re.sub(f"frac{pattern}{pattern}", r"frac\1\2", line)
    line = re.sub(f"frac{pattern}", r"frac\1", line)
    return line
