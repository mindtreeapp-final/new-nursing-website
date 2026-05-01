import os
import re

for root, dirs, files in os.walk(r'd:\editable web'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            def replacer(match):
                url = match.group(1)
                # Ensure it has .html
                if 'mindtreenursing.com' in url and not url.endswith('.html'):
                    new_url = url + '.html'
                    return match.group(0).replace(url, new_url)
                return match.group(0)
            
            # matches canonical tags, capturing the href value
            new_content = re.sub(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>', replacer, content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Fixed canonical in {filepath}')
