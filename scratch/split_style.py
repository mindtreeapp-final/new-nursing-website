import re

with open('d:/editable web/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Define sections to extract
index_sections = [
    "/* Hero Banner Redesign - Rising Tide Style */",
    "/* Rating Badge */",
    "/* Google Reviews Badge */",
    "/* New Stats Row */",
    "/* Visual Center - The Graphic Part */",
    "/* The Big Gradient Circle */",
    "/* The White Box Feature */",
    "/* Floating Cards */",
    "/* Services Section */",
    "/* Popular Courses Section */",
    "/* Offers Section */",
    "/* Explore Courses Section */",
    "/* Gallery Section */",
    "/* Lightbox Styles */",
    "/* ACHIEVEMENT BADGES SECTION */"
]

# We will split the content by lines and extract blocks
lines = content.split('\n')
global_css = []
index_css = []

current_target = global_css
i = 0
while i < len(lines):
    line = lines[i]
    is_section_header = False
    
    # Check if this line is an index section header
    for section in index_sections:
        if section in line:
            current_target = index_css
            is_section_header = True
            break
            
    # Check if we should switch back to global.
    # The sections that follow index sections and are global:
    if "/* Modal Styles */" in line or "/* Form Styles */" in line or "/* Fixed Action Buttons */" in line or "/* Registration Modal Styles */" in line or "/* Footer */" in line or "/* Responsive Design */" in line or "/* Notification Badge */" in line:
        current_target = global_css
        is_section_header = True
        
    current_target.append(line)
    i += 1

with open('d:/editable web/css/index.css', 'w', encoding='utf-8') as f:
    f.write('\n'.join(index_css))

with open('d:/editable web/css/global.css', 'w', encoding='utf-8') as f:
    f.write('\n'.join(global_css))

print("Split completed.")
