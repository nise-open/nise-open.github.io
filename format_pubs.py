import re

def rewrite_pub(file_path, is_zh=False):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into highlighted and all
    parts = re.split(r'## All|## 全部精选', content)
    if len(parts) != 2:
        print("Could not parse", file_path)
        return
    
    header_highlight = parts[0]
    all_pubs = parts[1]

    # Reconstruct headers
    new_content = ""
    if is_zh:
        new_content += "---\ntitleTemplate: 智能计算系统实验室\noutline: 3\n---\n\n# 精选文章\n\n## 重点推荐\n\n"
    else:
        new_content += "---\noutline: 3\n---\n\n# Selected Publications\n\n## Highlighted\n\n"

    # Add highlighted manually or parse them
    # Let's just keep highlighted as they are but cleaner
    new_content += """- **LEGO+: Redefining the Redundancy Removal for IoT Sensing Edge-End Systems** [ACM MobiSys '25]
  Chong Zhang, Han Wang, Qianhe Meng, Yize Zhao, Yihang Song, Kanglin Xu, Jinzhe Li, **Li Lu**

- **Hedgehog: Pushing the Range Limits of Ultrasonic Microphone Jammers** [ACM MobiCom '25]
  Shengyu Li, Mengchen Teng, Boyu Li, Songfan Li, Xiandong Shao, Chong Zhang, **Li Lu**

- **Processor-Sharing Internet of Things Architecture for Large-scale Deployment** [ACM SenSys '24] <span style="color: red; font-weight: bold;">*(Best Paper Award)*</span>
  Qianhe Meng, Han Wang, Chong Zhang, Yihang Song, Songfan Li, **Li Lu**, Hongzi Zhu

"""

    if is_zh:
        new_content += "## 全部精选\n\n"
    else:
        new_content += "## All Publications\n\n"

    # Now parse All publications
    years = re.split(r'### (\d{4})', all_pubs)
    
    for i in range(1, len(years), 2):
        year = years[i]
        pubs_block = years[i+1]
        new_content += f"### {year}\n\n"
        
        # Parse papers
        papers = re.split(r'#### (.*)', pubs_block)
        for j in range(1, len(papers), 2):
            title = papers[j].strip()
            details = papers[j+1].strip().split('\n')
            
            new_content += f"- **{title}**\n"
            
            for line in details:
                line = line.strip()
                if not line:
                    continue
                # Bold Li Lu
                line = re.sub(r'\bLi Lu\b', '**Li Lu**', line)
                line = re.sub(r'\b鲁力\b', '**鲁力**', line)
                new_content += f"  {line}\n"
            new_content += "\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

rewrite_pub('en/publication.md', False)
rewrite_pub('zh/publication.md', True)
