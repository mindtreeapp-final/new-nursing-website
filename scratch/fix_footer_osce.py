import os
import re

def fix_footer_formatting(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find the mangled footer links
    # <li><a href="...">OSCE KERALA</a>\n                            <a href="...">OSCE NEWZEALAND</a></li>
    mangled_pattern = re.compile(
        r'<li>(<a href="[^"]*?best-osce-coaching-in-kerala\.html">OSCE KERALA</a>)\s*(<a href="[^"]*?best-osce-coaching-in-newzealand\.html">OSCE NEWZEALAND</a>)</li>',
        re.DOTALL
    )
    
    def repl_footer(match):
        link1 = match.group(1)
        link2 = match.group(2)
        return f'<li>{link1}</li>\n                        <li>{link2}</li>'

    new_content = mangled_pattern.sub(repl_footer, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    root_dir = r'd:\web build'
    count = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if fix_footer_formatting(file_path):
                    print(f"Fixed {file_path}")
                    count += 1
    print(f"Total files fixed: {count}")

if __name__ == "__main__":
    main()
