import re

updates = {
    'osce-training-kerala.html': {
        'title': 'OSCE Training in Kerala | Mindtree Nursing',
        'desc': 'Best OSCE training institute in Kerala with simulation lab and expert trainers.',
        'h1': 'Best OSCE Training in Kerala'
    },
    'iqn-course-new-zealand.html': {
        'title': 'IQN Course New Zealand | Mindtree Nursing',
        'desc': 'Top IQN course for New Zealand nursing registration. Complete guidance and coaching.',
        'h1': 'IQN Course New Zealand'
    },
    'oet-coaching-india.html': {
        'title': 'OET Coaching in India | Mindtree Nursing',
        'desc': 'Premium OET coaching in India for nurses aiming to work abroad. Experienced trainers and comprehensive materials.',
        'h1': 'OET Coaching in India'
    },
    'nursing-abroad-consultancy.html': {
        'title': 'Nursing Abroad Consultancy | Mindtree Nursing',
        'desc': 'Expert nursing abroad consultancy providing guidance on study abroad, New Zealand nursing registration, and international placements.',
        'h1': 'Nursing Abroad Consultancy'
    }
}

for file, data in updates.items():
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update <title>
        content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', content, flags=re.DOTALL)
        
        # Update <meta name="description">
        # Sometimes there's newlines, we should be careful.
        content = re.sub(r'<meta\s+name="description"\s+content="[^"]*">', f'<meta name="description"\n        content="{data["desc"]}">', content)
        
        # Update <h1>
        # We assume <h1> is structured like <h1>...</h1>
        content = re.sub(r'<h1>.*?</h1>', f'<h1>{data["h1"]}</h1>', content, count=1, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated metadata for {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

