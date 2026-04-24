import re

updates = {
    'index.html': {
        'title': 'Mindtree Nursing Solutions | OET, IQN & OSCE Training for Nurses',
        'desc': 'Mindtree Nursing Solutions offers expert consultancy and coaching for OET, IQN, and OSCE to help nurses register and work in New Zealand and abroad.',
    },
    'ichc-guide-nursing-registration.html': {
        'title': 'ICHC Guide for Nursing Registration | International Criminal History Check',
        'desc': 'Ultimate guide to the ICHC (International Criminal History Check) process for overseas nurses seeking international registration.',
        'h1': 'ICHC Guide for Nursing Registration'
    },
    'nursing-interview-assistance.html': {
        'title': 'Nursing Interview Assistance & Preparation | Mindtree Nursing',
        'desc': 'Get expert nursing interview assistance. Prepare for international hospital placements with confidence through our targeted coaching.',
        'h1': 'Nursing Interview Assistance & Preparation'
    },
    'therapeutic-communication-nursing.html': {
        'title': 'Therapeutic Communication Course for Nurses | Mindtree Nursing',
        'desc': 'Master therapeutic communication skills essential for international nursing. Improve patient interactions and pass communication assessments.',
        'h1': 'Therapeutic Communication Course for Nurses'
    }
}

for file, data in updates.items():
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update <title>
        content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', content, flags=re.DOTALL)
        
        # Update <meta name="description">
        content = re.sub(r'<meta\s+name="description"\s+content="[^"]*">', f'<meta name="description"\n        content="{data["desc"]}">', content)
        
        if 'h1' in data:
            # Update <h1>
            content = re.sub(r'<h1>.*?</h1>', f'<h1>{data["h1"]}</h1>', content, count=1, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated metadata for {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")
