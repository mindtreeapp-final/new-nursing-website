import re

with open("d:/editable web/blog/the-benefits-of-choosing-mindtree-nursing-solution-for-your-career-growth.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace metadata
html = re.sub(
    r'<title>.*?</title>',
    '<title>The Success Stories of Nurses Who Have Chosen Mindtree Nursing Solution for Their Careers | Mindtree Nursing Solutions</title>',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<meta name="description"\s+content="[^"]*">',
    '<meta name="description"\n        content="Discover the success stories of nurses who achieved their career goals with Mindtree Nursing Solutions, securing global placements and navigating licensure processes.">',
    html
)

html = re.sub(
    r'<meta name="keywords"\s+content="[^"]*">',
    '<meta name="keywords"\n        content="Mindtree Nursing Solution success stories, nursing career growth, New Zealand nursing jobs, Australia nursing jobs, CGFNS process support, nursing career success">',
    html
)

html = re.sub(
    r'<link rel="canonical"\s+href="[^"]*">',
    '<link rel="canonical"\n        href="https://www.mindtreenursing.com/blog/the-success-stories-of-nurses-who-have-chosen-mindtree-nursing-solution-for-their-careers">',
    html
)

html = re.sub(
    r'<meta property="og:title" content="[^"]*">',
    '<meta property="og:title" content="The Success Stories of Nurses Who Have Chosen Mindtree Nursing Solution for Their Careers">',
    html
)

html = re.sub(
    r'<meta property="og:description"\s+content="[^"]*">',
    '<meta property="og:description"\n        content="Discover the success stories of nurses who achieved their career goals with Mindtree Nursing Solutions, securing global placements and navigating licensure processes.">',
    html
)

html = re.sub(
    r'<meta property="og:url"\s+content="[^"]*">',
    '<meta property="og:url"\n        content="https://www.mindtreenursing.com/blog/the-success-stories-of-nurses-who-have-chosen-mindtree-nursing-solution-for-their-careers">',
    html
)

html = re.sub(
    r'<meta name="twitter:title" content="[^"]*">',
    '<meta name="twitter:title" content="The Success Stories of Nurses Who Have Chosen Mindtree Nursing Solution for Their Careers">',
    html
)

html = re.sub(
    r'<meta name="twitter:description"\s+content="[^"]*">',
    '<meta name="twitter:description"\n        content="Discover the success stories of nurses who achieved their career goals with Mindtree Nursing Solutions, securing global placements and navigating licensure processes.">',
    html
)

html = re.sub(
    r'"headline": "[^"]*"',
    '"headline": "The Success Stories of Nurses Who Have Chosen Mindtree Nursing Solution for Their Careers"',
    html
)

html = re.sub(
    r'"description": "[^"]*"',
    '"description": "Discover the success stories of nurses who achieved their career goals with Mindtree Nursing Solutions, securing global placements and navigating licensure processes."',
    html
)

html = re.sub(
    r'"datePublished": "[^"]*"',
    '"datePublished": "2026-04-24"',
    html
)

html = re.sub(
    r'"url": "https://www.mindtreenursing.com/blog/[^"]*"',
    '"url": "https://www.mindtreenursing.com/blog/the-success-stories-of-nurses-who-have-chosen-mindtree-nursing-solution-for-their-careers"',
    html
)

html = re.sub(
    r'"@id": "https://www.mindtreenursing.com/blog/[^"]*"',
    '"@id": "https://www.mindtreenursing.com/blog/the-success-stories-of-nurses-who-have-chosen-mindtree-nursing-solution-for-their-careers"',
    html
)

# Replace Hero
html = html.replace(
    '<h1>The Benefits of Choosing Mindtree Nursing Solution for Your Career Growth</h1>',
    '<h1>The Success Stories of Nurses Who Have Chosen Mindtree Nursing Solution for Their Careers</h1>'
)

html = html.replace(
    '<span><i class="fas fa-calendar-alt"></i> April 14, 2026</span>',
    '<span><i class="fas fa-calendar-alt"></i> April 24, 2026</span>'
)

html = html.replace(
    '<span><i class="fas fa-tag"></i> Why Choose Us</span>',
    '<span><i class="fas fa-tag"></i> Success Stories</span>'
)

html = html.replace(
    '<span><i class="fas fa-clock"></i> 5 min read</span>',
    '<span><i class="fas fa-clock"></i> 3 min read</span>'
)

# Find the block to replace using regex, but then use simple assignment for the content
content_regex = re.compile(r'<img src="\.\./images/mainpage/subpage/MTREE\.jpg".*?<div class="back-to-blog".*?</div>', re.DOTALL)
match = content_regex.search(html)

if match:
    start, end = match.span()
    new_content = """<img src="../images/mainpage/subpage/MTREE.jpg"
                        alt="Success Stories of Nurses Choosing Mindtree Nursing Solutions"
                        class="blog-featured-image" />

                    <p>Mindtree Nursing Solution has witnessed numerous success stories of nurses who have chosen their services for their careers. From securing prestigious job placements in countries like New Zealand and Australia to successfully navigating the CGFNS and nursing council processes, nurses have achieved their goals with Mindtree's support.</p>
                    
                    <div class="intro-banner">
                        <div class="banner-icon">
                            <i class="fas fa-trophy"></i>
                        </div>
                        <p>The personalised guidance, access to global study opportunities, and comprehensive training programs have empowered nurses to excel in their professions.</p>
                    </div>

                    <p>These success stories highlight Mindtree Nursing Solution's commitment to fostering the growth and success of nurses, making it a trusted choice for those seeking a fulfilling and rewarding career in the field of nursing.</p>

                    <div class="back-to-blog" style="margin-top: 44px;">
                        <a href="index.html"><i class="fas fa-arrow-left"></i> Back to Blog</a>
                    </div>"""
    html = html[:start] + new_content + html[end:]

# Fix navbar Blog link
html = html.replace('<li><a href="../index" class="active">Blog</a></li>', '<li><a href="index.html" class="active">Blog</a></li>')
html = html.replace('<li><a href="../index">Blog</a></li>', '<li><a href="index.html">Blog</a></li>')
html = html.replace('<a href="blog\\index">', '<a href="index.html">')

with open("d:/editable web/blog/the-success-stories-of-nurses-who-have-chosen-mindtree-nursing-solution-for-their-careers.html", "w", encoding="utf-8") as f:
    f.write(html)
print("File created successfully")
