import os
import re

blog_dir = "d:/editable web/blog"
files = [f for f in os.listdir(blog_dir) if f.endswith(".html") and f != "index.html"]

new_sidebar_items = [
    {
        "url": "osce-simulation-tools-resources",
        "img": "../images/mainpage/subpage/1.jpg",
        "title": "OSCE Simulation Tools"
    },
    {
        "url": "osce-exam-survival-guide-tips",
        "img": "../images/mainpage/subpage/1.jpg",
        "title": "OSCE Exam Survival Guide"
    },
    {
        "url": "ahpra-registration-update-iqrn",
        "img": "../images/mainpage/migration.jpg",
        "title": "AHPRA Registration: 2025 Update"
    }
]

for filename in files:
    filepath = os.path.join(blog_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    items_to_add = []
    for item in new_sidebar_items:
        if item["url"] not in filename:
            if item["url"] not in content:
                item_html = f"""                    <a href="{item['url']}" class="recent-blog-item">
                        <img src="{item['img']}" alt="{item['title']}" class="recent-blog-thumb" />
                        <div class="recent-blog-info">
                            <h5>{item['title']}</h5>
                        </div>
                    </a>
"""
                items_to_add.append(item_html)

    if items_to_add:
        added_html = "".join(items_to_add)
        content = re.sub(
            r'(<h4>Recent Blogs</h4>\s*)',
            r'\1' + added_html,
            content,
            count=1
        )
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated sidebar in {filename}")

print("Sidebar updates complete.")
