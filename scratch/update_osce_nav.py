import os
import re

def update_nav_and_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine if we are in the blog directory (need ../)
    is_blog = 'blog' in file_path.lower()
    prefix = '../' if is_blog else ''

    # 1. Update Dropdown
    # Old dropdown pattern:
    # <div class="dropdown-content">
    #     <a href="oet.html">OET</a>
    #     <a href="iqn.html">IQN</a>
    #     <a href="osce.html">OSCE</a>
    #     <a href="therapeutic.html">Therapeutic Communication</a>
    #     <a href="interview.html">Interview Assistance</a>
    # </div>
    
    dropdown_pattern = re.compile(
        r'(<div class="dropdown-content">.*?<a href="[^"]*?osce\.html"[^>]*?>OSCE</a>)(.*?</div>)',
        re.DOTALL
    )
    
    def repl_dropdown(match):
        pre = match.group(1)
        post = match.group(2)
        
        # Replace the osce.html link with the two new ones
        pre = re.sub(
            r'<a href="([^"]*?)osce\.html"[^>]*?>OSCE</a>',
            f'<a href="\\1best-osce-coaching-in-kerala.html">OSCE KERALA</a>\n                            <a href="\\1best-osce-coaching-in-newzealand.html">OSCE NEWZEALAND</a>',
            pre
        )
        return pre + post

    content = dropdown_pattern.sub(repl_dropdown, content)

    # 2. Update Footer Link
    # <li><a href="osce.html">OSCE</a></li>
    footer_pattern = re.compile(r'<li><a href="([^"]*?)osce\.html">OSCE</a></li>')
    content = footer_pattern.sub(
        f'<li><a href="\\1best-osce-coaching-in-kerala.html">OSCE KERALA</a></li>\n                        <li><a href="\\1best-osce-coaching-in-newzealand.html">OSCE NEWZEALAND</a></li>',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    root_dir = r'd:\web build'
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"Updating {file_path}")
                update_nav_and_footer(file_path)

if __name__ == "__main__":
    main()
