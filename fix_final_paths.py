import os
import re

blog_dir = r"d:\web build\blog"
root_pages = [
    "index.html", "about.html", "oet.html", "iqn.html", "osce.html", 
    "therapeutic.html", "interview.html", "premium-landing.html", 
    "course-detail.html", "about-us.html" # adding common duplicates just in case
]

# Asset directories to prefix
asset_dirs = ["images", "css", "js"]

for file in os.listdir(blog_dir):
    if not file.endswith(".html"):
        continue
    
    path = os.path.join(blog_dir, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix Image/CSS/JS paths
    for asset in asset_dirs:
        # Match src="images/..." or href="css/..." or src="images\..." etc.
        # But specifically those NOT already prefixed with ../
        # Pattern: (src|href)=["'](asset)[\\/].*?["']
        pattern = r'(src|href)=([\'"])(?!https?:\/\/|mailto:|\/|#|\.\.\/)(' + re.escape(asset) + r'[\\/].*?)([\'"])'
        content = re.sub(pattern, r'\1=\2../\3\4', content)

    # 2. Fix Root Page links
    for root_page in root_pages:
        # Pattern: href=["']root_page["'] (but not already prefixed)
        pattern = r'href=([\'"])(?!https?:\/\/|mailto:|\/|#|\.\.\/)(' + re.escape(root_page) + r')([\'"])'
        content = re.sub(pattern, r'href=\1../\2\3', content)

    # 3. Remove "blog/" prefix from internal blog links
    # If a file in blog/ links to "blog/something.html", it should just be "something.html"
    content = re.sub(r'href=([\'"])blog\/([^"\']+?)([\'"])', r'href=\1\2\3', content)

    # 4. Normalize backslashes in paths to forward slashes for web compatibility
    # Specifically inside src and href attributes
    def normalize_slashes(match):
        return match.group(0).replace('\\', '/')
    
    content = re.sub(r'(src|href)=([\'"]).*?([\'"])', normalize_slashes, content)

    # 5. Fix specific known broken links like link to favicon or style.css that might be missing ../
    # (The general asset loop above should catch most, but these are common)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Processed {file}")

print("Done")
