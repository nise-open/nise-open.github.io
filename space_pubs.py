import re

def parse_and_space(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    in_list_item = False
    
    for line in lines:
        stripped = line.strip()
        if line.startswith('- **'):
            in_list_item = True
            new_lines.append(line)
            continue
        
        if in_list_item:
            if stripped == '':
                # End of list item
                in_list_item = False
                new_lines.append(line)
            else:
                # Add an empty line before this attribute to make it a new paragraph
                if not new_lines[-1].strip() == '':
                    new_lines.append('  \n')
                new_lines.append(line)
        else:
            new_lines.append(line)

    # Let's write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

parse_and_space('en/publication.md')
parse_and_space('zh/publication.md')
