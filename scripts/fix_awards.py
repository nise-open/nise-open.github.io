import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace inline red best paper with gold badge
    content = content.replace(
        '<span style="color: red; font-weight: bold;">*(Best Paper Award)*</span>',
        '<span class="gold-badge">*(Best Paper Award)*</span>'
    )
    
    # Replace markdown **Best Paper Award** with gold badge
    content = content.replace(
        '**Best Paper Award**',
        '<span class="gold-badge">Best Paper Award</span>'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('en/publication.md')
update_file('zh/publication.md')
