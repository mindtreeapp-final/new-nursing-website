import os
import glob

html_files = glob.glob('*.html') + glob.glob('blog/*.html')

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace style.css with global.css
    content = content.replace('href="css/style.css"', 'href="css/global.css"')
    content = content.replace('href="../css/style.css"', 'href="../css/global.css"')
    
    # If it's index.html, add index.css
    if os.path.basename(html_file) == 'index.html':
        if 'blog/index.html' in html_file.replace('\\', '/'):
            pass
        else:
            # Add index.css after global.css
            content = content.replace('<link rel="stylesheet" href="css/global.css">', '<link rel="stylesheet" href="css/global.css">\n    <link rel="stylesheet" href="css/index.css">')
            
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files to use global.css")
