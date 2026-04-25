import os

blog_dir = "d:/editable web/blog"
files = [f for f in os.listdir(blog_dir) if f.endswith(".html")]

for filename in files:
    filepath = os.path.join(blog_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix Blog link in navbar
    # Target: <li><a href="../index" class="active">Blog</a></li>
    # Replacement: <li><a href="index.html" class="active">Blog</a></li>
    # Also handle variants without .html if needed
    
    new_content = content.replace('<li><a href="../index" class="active">Blog</a></li>', '<li><a href="index.html" class="active">Blog</a></li>')
    new_content = new_content.replace('<li><a href="../index">Blog</a></li>', '<li><a href="index.html">Blog</a></li>')
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed navbar in {filename}")

print("Navbar fixes complete.")
