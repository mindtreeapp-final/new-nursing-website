import os
import re

def clean_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find href="..." where it ends with .html and does not start with http
    # Also ignore .html in the middle of a string, we only want href="....html" or href="....html#..."
    # Actually, let's just do a simple replacement for hrefs ending in .html
    def replacer(match):
        url = match.group(1)
        if url.startswith('http') or url.startswith('mailto:') or url.startswith('tel:'):
            return match.group(0) # Keep as is
        
        # Remove .html
        if url.endswith('.html'):
            new_url = url[:-5]
        elif '.html#' in url:
            new_url = url.replace('.html#', '#')
        else:
            return match.group(0)

        # For index, maybe replace with just the folder? e.g. "index" -> ""?
        # Vercel handles /index as / anyway, but just leaving it as "index" or "../index" is fine.
        return f'href="{new_url}"'

    new_content = re.sub(r'href="([^"]+\.html(?:#[^"]*)?)"', replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

def main():
    base_dir = r"d:\web build"
    for root, dirs, files in os.walk(base_dir):
        if 'scratch' in root or '.git' in root or '.vscode' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                clean_links(os.path.join(root, file))

if __name__ == '__main__':
    main()
