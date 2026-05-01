import os
import re

base_url = "https://www.mindtreenursing.com/"

for root, dirs, files in os.walk(r'd:\editable web'):
    # Skip scratch
    if 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            # relative path from root
            rel_path = os.path.relpath(filepath, r'd:\editable web').replace('\\', '/')
            expected_canonical = base_url + rel_path
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content
            
            # Check if canonical exists
            canonical_match = re.search(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*>', content)
            if canonical_match:
                # Replace existing canonical
                new_tag = f'<link rel="canonical" href="{expected_canonical}">'
                new_content = new_content.replace(canonical_match.group(0), new_tag)
            else:
                # Add canonical before </head>
                if '</head>' in new_content:
                    new_tag = f'    <link rel="canonical" href="{expected_canonical}">\n</head>'
                    new_content = new_content.replace('</head>', new_tag)

            # Fix blog/best-osce-coaching-in-kerala.html title
            if rel_path == 'blog/best-osce-coaching-in-kerala.html':
                new_content = re.sub(
                    r'<title>.*?</title>',
                    '<title>Best OSCE Coaching in Kerala | Mindtree Nursing Solutions</title>',
                    new_content,
                    flags=re.DOTALL
                )

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated canonical/SEO for {rel_path}")

print("SEO update complete.")
