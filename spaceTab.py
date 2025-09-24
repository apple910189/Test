import pathlib, re

tabsize = 4

for path in pathlib.Path(".").rglob("*.py"):
	text = path.read_text()
	def convert_indent(match):
		s = match.group(0)
		# 先把 tabs 換算成空格長度，再轉回 tabs
		spaces = 0
		for ch in s:
			if ch == "\t":
				spaces += tabsize
			else:
				spaces += 1
		return "\t" * (spaces // tabsize) + " " * (spaces % tabsize)
	new_text = re.sub(r'^[\t ]+', convert_indent, text, flags=re.M)
	path.write_text(new_text)
