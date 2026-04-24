import os
import re
import shutil

ROOT_DIR = r"d:\web build"
BLOG_DIR = os.path.join(ROOT_DIR, "blog")

if not os.path.exists(BLOG_DIR):
    os.makedirs(BLOG_DIR)

DUPLICATE_MAP = {
    "oet-coaching-india.html": "oet.html",
    "iqn-course-new-zealand.html": "iqn.html",
    "osce-training-kerala.html": "osce.html",
    "therapeutic-communication-nursing.html": "therapeutic.html",
    "nursing-interview-assistance.html": "interview.html",
    "ichc-guide-nursing-registration.html": "ichc-blog.html",
    "about-us.html": "about.html",
    "nursing-abroad-consultancy.html": "about.html",
    "blog.html": "blog/index.html"
}

BLOG_FILES = [
    "choosing-your-migration-partner-a-comprehensive-guide-for-students.html",
    "conquering-the-oet-landscape-a-nurse-s-guide-to-success.html",
    "embracing-the-kiwi-way-tips-for-international-nurses-moving-to-new-zealand.html",
    "ensuring-competence-new-zealand-s-revamped-assessment-for-international-nurses.html",
    "navigating-the-registration-process-for-internationally-qualified-nurses-in-new-zealand.html",
    "the-benefits-of-choosing-mindtree-nursing-solution-for-your-career-growth.html",
    "the-success-stories-of-nurses-who-have-chosen-mindtree-nursing-solution-for-their-careers.html",
    "understanding-cgfns-an-essential-guide-for-international-nurses.html",
    "understanding-osce-a-comprehensive-guide-for-internationally-qualified-nurses.html",
    "what-internationally-qualified-nurses-need-to-know.html",
    "what-is-mindtree-nursing-solution-and-what-it-offers.html",
    "why-is-mindtree-nursing-solution-the-best-choice-for-your-career.html",
    "ichc-blog.html",
    "trumerit-for-newzealand-nursing-registration.html"
]

def fix_links_for_root(content):
    # First, replace duplicate names
    for old, new in DUPLICATE_MAP.items():
        # Match href="old" or href='old'
        content = re.sub(r'(href=["\'])' + re.escape(old) + r'(["\'])', r'\1' + new + r'\2', content)
        
    return content

def fix_links_for_blog_subdir(content):
    content = fix_links_for_root(content)
    # Prefix relative paths with ../ 
    # Things to prefix: images/, css/, js/
    content = re.sub(r'(href=["\'])css/', r'\1../css/', content)
    content = re.sub(r'(src=["\'])js/', r'\1../js/', content)
    content = re.sub(r'(src=["\']|href=["\'])images/', r'\1../images/', content)
    # Also link to style.css directly ? Wait, only css/style.css is used mostly, but let's fix /style.css to ../css/style.css
    content = content.replace('href="/style.css"', 'href="../css/style.css"')
    
    # HTML files in root
    root_htmls = [
        "index.html", "about.html", "oet.html", "iqn.html", "osce.html", 
        "therapeutic.html", "interview.html", "premium-landing.html"
    ]
    for h in root_htmls:
        # We only want to replace standalone links to these root files, not if they're already ../
        # If it matches href="index.html" it should become href="../index.html"
        content = re.sub(r'(href=["\'])' + re.escape(h) + r'(["\'])', r'\1../' + h + r'\2', content)
        
    # blog/index.html -> index.html (since we are already in blog/)
    content = re.sub(r'(href=["\'])blog/index.html(["\'])', r'\1index.html\2', content)
    # other blog references? href="blog/..." -> href="..."
    content = re.sub(r'(href=["\'])blog/([^"]+)(["\'])', r'\1\2\3', content)

    # Note: <form action="..."> might need adjustment if present, but typically not.
    return content

# 1. Delete duplicate files
for old_name in DUPLICATE_MAP.keys():
    if old_name == "blog.html" or old_name == "about-us.html" or old_name == "nursing-abroad-consultancy.html":
        pass # Handle blog.html by modifying/moving. The others don't exist physically.
    else:
        file_path = os.path.join(ROOT_DIR, old_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {old_name}")

# Delete root duplicates of blog files if they exist in blog/ too? Wait, we'll just move them.
# BUT wait! If ichc-blog.html is in DUPLICATE_MAP target, it shouldn't be deleted.

# 2. Modify and maybe move blog.html
blog_html_path = os.path.join(ROOT_DIR, "blog.html")
if os.path.exists(blog_html_path):
    with open(blog_html_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = fix_links_for_blog_subdir(content)
    with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    os.remove(blog_html_path)
    print("Moved and updated blog.html -> blog/index.html")

# 3. Process all remaining files in ROOT_DIR
for file in os.listdir(ROOT_DIR):
    if file.endswith(".html"):
        path = os.path.join(ROOT_DIR, file)
        
        # Is it a blog post?
        if file in BLOG_FILES:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            content = fix_links_for_blog_subdir(content)
            
            dest_path = os.path.join(BLOG_DIR, file)
            with open(dest_path, "w", encoding="utf-8") as f:
                f.write(content)
            os.remove(path)
            print(f"Moved and updated {file} -> blog/{file}")
        else:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            content = fix_links_for_root(content)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {file} in root")

# Process any files ALREADY in blog folder (e.g. they might have been moved previously)
for file in os.listdir(BLOG_DIR):
    if file.endswith(".html") and file != "index.html" and file not in BLOG_FILES:
        # Wait, if `trumerit...` was already in there, we process it.
        # But we actually want to process ALL files in BLOG_DIR just to be safe.
        pass

for file in os.listdir(BLOG_DIR):
    if file.endswith(".html"):
        path = os.path.join(BLOG_DIR, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # To be safe, let's run fix_links_for_blog_subdir on them again. But wait, if they already have ../images, it will become ../../images!
        # So we should be careful not to double-prefix.
        content = content.replace("href=\"../css/", "href=\"css/")
        content = content.replace("href='../css/", "href='css/")
        content = content.replace("src=\"../js/", "src=\"js/")
        content = content.replace("src='../js/", "src='js/")
        content = content.replace("href=\"../images/", "href=\"images/")
        content = content.replace("src=\"../images/", "src=\"images/")
        
        # Same for html
        for h in ["index.html", "about.html", "oet.html", "iqn.html", "osce.html", "therapeutic.html", "interview.html", "premium-landing.html"]:
            content = content.replace(f'href="../{h}"', f'href="{h}"')
            content = content.replace(f"href='../{h}'", f"href='{h}'")
            
        content = fix_links_for_blog_subdir(content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Verified/updated {file} in blog/")

print("Done!")
