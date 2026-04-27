import re

with open('d:/editable web/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all comments that start at the beginning of a line
comments = re.findall(r'^/\*.*?\*/', content, re.MULTILINE)
for c in comments:
    print(c)
