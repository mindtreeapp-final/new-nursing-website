import os
import re
import glob

files_to_rename = {
    'osce.html': 'osce-training-kerala.html',
    'iqn.html': 'iqn-course-new-zealand.html',
    'oet.html': 'oet-coaching-india.html',
    'about.html': 'nursing-abroad-consultancy.html'
}

html_files = glob.glob('*.html')

# 1. Update contents
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for old, new in files_to_rename.items():
        content = content.replace(f'"{old}"', f'"{new}"')
        content = content.replace(f'"{old}#', f'"{new}#')
        
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {file}")

# 2. Rename files
for old, new in files_to_rename.items():
    if os.path.exists(old):
        os.rename(old, new)
        print(f"Renamed {old} to {new}")
