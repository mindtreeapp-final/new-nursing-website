import os
import re

html_files = []
for root, dirs, files in os.walk(r"d:\editable web"):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

pages = [
    "about",
    "best-osce-coaching-in-kerala",
    "best-osce-coaching-in-newzealand",
    "contact",
    "index",
    "interview",
    "iqn",
    "oet",
    "osce",
    "premium-landing",
    "therapeutic",
    "ahpra-registration-update-iqrn",
    "choosing-your-migration-partner-a-comprehensive-guide-for-students",
    "ichc",
    "osce-exam-survival-guide-tips",
    "osce-simulation-tools-resources",
    "tech-meets-care-how-technology-is-shaping-modern-nursing-in-new-zealand",
    "the-benefits-of-choosing-mindtree-nursing-solution-for-your-career-growth",
    "the-success-stories-of-nurses-who-have-chosen-mindtree-nursing-solution-for-their-careers",
    "trumerit-for-newzealand-nursing-registration",
    "why-is-mindtree-nursing-solution-the-best-choice-for-your-career"
]

def fix_hrefs(content):
    def replacer(match):
        href = match.group(1)
        
        # Check if it has an anchor
        parts = href.split('#')
        base_href = parts[0]
        hash_part = f"#{parts[1]}" if len(parts) > 1 else ""
        
        if not base_href:
            return match.group(0) # it's just an anchor like href="#section"

        # Extract the page name (ignoring path parts)
        page_name = base_href.split('/')[-1]
        
        if page_name in pages and not base_href.endswith('.html'):
            new_href = base_href + ".html" + hash_part
            return f'href="{new_href}"'
            
        return match.group(0)

    # Use regex to find all href attributes
    new_content = re.sub(r'href="([^"]+)"', replacer, content)
    return new_content

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = fix_hrefs(content)
    
    if new_content != content:
        print(f"Fixed {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
