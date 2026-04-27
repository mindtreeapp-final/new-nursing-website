import os
import re
import glob

html_files = glob.glob('*.html') + glob.glob('blog/*.html')
css_dir = 'css'

os.makedirs(css_dir, exist_ok=True)

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if there's a <style> block
    style_matches = list(re.finditer(r'<style>(.*?)</style>', content, re.DOTALL))
    if not style_matches:
        continue
    
    # We will extract all style blocks into one CSS file for the page
    css_content = ""
    for match in style_matches:
        css_content += match.group(1).strip() + "\n\n"
    
    # Create the new CSS file
    base_name = os.path.basename(html_file).replace('.html', '')
    if 'blog' in html_file:
        css_filename = f"blog-{base_name}.css"
        css_filepath = os.path.join(css_dir, css_filename)
        link_tag = f'<link rel="stylesheet" href="../css/{css_filename}">'
    else:
        css_filename = f"{base_name}.css"
        css_filepath = os.path.join(css_dir, css_filename)
        link_tag = f'<link rel="stylesheet" href="css/{css_filename}">'
    
    with open(css_filepath, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    # Remove the style blocks and add the link tag in head
    # Replace the first style block with the link tag, and remove others
    new_content = content
    for i, match in enumerate(style_matches):
        if i == 0:
            new_content = new_content.replace(match.group(0), link_tag)
        else:
            new_content = new_content.replace(match.group(0), '')
            
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Extracted styles from {html_file} to {css_filepath}")

