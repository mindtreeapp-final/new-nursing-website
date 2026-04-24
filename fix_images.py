import os
import re

blog_dir = r"d:\web build\blog"

for file in os.listdir(blog_dir):
    if file.endswith(".html"):
        path = os.path.join(blog_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Match src="images\... " or src="images/... " replacing with src="../images/... "
        # First we might find things like src="images\mainpage\subpage\1.jpg"
        
        # We need to turn any src="images\..." or src="images/..." to src="../images/..."
        # If it ALREADY starts with src="../images/" we leave it alone.
        
        def replace_img(match):
            # match.group(0) is the full match like src="images\mainpage\subpage\1.jpg"
            # match.group(1) is the quote " or '
            # match.group(2) is the path after images
            quote = match.group(1)
            path_part = match.group(2)
            # convert backslashes to forward slashes
            path_part = path_part.replace('\\', '/')
            return f'src={quote}../images{path_part}'
            
        new_content = re.sub(r'src=(["\'])images([\\/].*?["\'])', replace_img, content)
        
        if new_content != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed images in {file}")

print("Done")
