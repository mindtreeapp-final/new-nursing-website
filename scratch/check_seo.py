import os
import re

files_to_check = [
    'best-osce-coaching-in-kerala.html',
    'osce.html',
    'iqn.html',
    'therapeutic.html',
    'interview.html'
]

# add blog pages
for root, dirs, files in os.walk('blog'):
    for f in files:
        if f.endswith('.html'):
            files_to_check.append('blog/' + f)

for filepath in files_to_check:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    robots = re.search(r'<meta[^>]*name=[\"\']robots[\"\'][^>]*content=[\"\']([^\"\']+)[\"\']', content)
    canonical = re.search(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*href=[\"\']([^\"\']+)[\"\']', content)
    title = re.search(r'<title>([^<]+)</title>', content)
    desc = re.search(r'<meta[^>]*name=[\"\']description[\"\'][^>]*content=[\"\']([^\"\']+)[\"\']', content)
    
    print(f'\nFile: {filepath}')
    print(f'Robots: {robots.group(1) if robots else "Missing"}')
    print(f'Canonical: {canonical.group(1) if canonical else "Missing"}')
    print(f'Title: {title.group(1) if title else "Missing"}')
    print(f'Desc: {bool(desc)}')
