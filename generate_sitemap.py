import glob
import os

html_files = glob.glob('*.html')
blog_files = glob.glob('blog/*.html')
base_url = "https://www.mindtreenursing.com/"

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for file in html_files + blog_files:
    # Use forward slash for web URL
    url_path = file.replace('\\', '/')
    
    if url_path == 'index.html':
        url = base_url
    elif url_path == 'blog/index.html':
        url = base_url + "blog"
    else:
        # Strip .html for the clean URL
        clean_name = url_path.replace('.html', '')
        url = base_url + clean_name
        
    sitemap += f"  <url>\n    <loc>{url}</loc>\n  </url>\n"

sitemap += '</urlset>'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
    
print("Sitemap generated.")
