import pathlib
import re

tabsize = 4  # 一個 tab 視為 4 個空格

for path in pathlib.Path(".").rglob("*.py"):
    text = path.read_text()
    
    def convert_indent(match):
        s = match.group(0)
        # 把 tab 和空格換算成總空格數
        spaces = 0
        for ch in s:
            if ch == "\t":
                spaces += tabsize
            else:
                spaces += 1
        # 換回「幾組完整 4 空格 + 餘下的空格」
        return " " * spaces
    
    new_text = re.sub(r'^[\t ]+', convert_indent, text, flags=re.M)
    path.write_text(new_text)
