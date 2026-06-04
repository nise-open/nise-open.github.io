import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. TMC 2025
    content = content.replace(
        "- **Embedding Chips Over the Air: Rethink IoT Architecture for Ubiquitous Sensing**\n  [DOI:10.1109/TMC.2025.3567635]",
        "- **Embedding Chips Over the Air: Rethink IoT Architecture for Ubiquitous Sensing**\n  Qianhe Meng, Han Wang, Chong Zhang, Yihang Song, Songfan Li, **Li Lu**, Hongzi Zhu\n  *IEEE Transactions on Mobile Computing (TMC 2025)*\n  [DOI:10.1109/TMC.2025.3567635]"
    )
    
    # Using generic match in case the bracket string is slightly different.
    replacements = [
        (
            "- **Embedding Chips Over the Air: Rethink IoT Architecture for Ubiquitous Sensing**\n  [DOI:10.1109/TMC.2025.3567635](https://doi.org/10.1109/TMC.2025.3567635)",
            "- **Embedding Chips Over the Air: Rethink IoT Architecture for Ubiquitous Sensing**\n  Qianhe Meng, Han Wang, Chong Zhang, Yihang Song, Songfan Li, **Li Lu**, Hongzi Zhu\n  *IEEE Transactions on Mobile Computing (TMC 2025)*\n  [DOI:10.1109/TMC.2025.3567635](https://doi.org/10.1109/TMC.2025.3567635)"
        ),
        (
            "- **Unilateral Control for Social Welfare of Iterated Game in Mobile Crowdsensing**\n  [DOI:10.1007/s11390-023-3041-0](https://doi.org/10.1007/s11390-023-3041-0)",
            "- **Unilateral Control for Social Welfare of Iterated Game in Mobile Crowdsensing**\n  Ji-Qing Gu, Chao Song, Jie Wu, **Li Lu**, Ming Liu\n  *Journal of Computer Science and Technology (JCST 2025)*\n  [DOI:10.1007/s11390-023-3041-0](https://doi.org/10.1007/s11390-023-3041-0)"
        ),
        (
            "- **A Compact Impedance Matching Layer for Dual-Band Implantable Medical Devices**\n  [DOI:10.1109/LAWP.2024.3424279](https://doi.org/10.1109/LAWP.2024.3424279)",
            "- **A Compact Impedance Matching Layer for Dual-Band Implantable Medical Devices**\n  Yibo Pan, Wenjie Fu, Dun Lu, Tongxing Huang, Yihang Song, **Li Lu**, Yang Yan\n  *IEEE Antennas and Wireless Propagation Letters (AWPL 2024)*\n  [DOI:10.1109/LAWP.2024.3424279](https://doi.org/10.1109/LAWP.2024.3424279)"
        ),
        (
            "- **A Lightweight and Chip-Level Reconfigurable Architecture for Next-Generation IoT End Devices**\n  [DOI:10.1109/TC.2023.3343094](https://doi.org/10.1109/TC.2023.3343094)",
            "- **A Lightweight and Chip-Level Reconfigurable Architecture for Next-Generation IoT End Devices**\n  Chong Zhang, Songfan Li, Yihang Song, Qianhe Meng, **Li Lu**, Hongzi Zhu, Xin Wang\n  *IEEE Transactions on Computers (TC 2024)*\n  [DOI:10.1109/TC.2023.3343094](https://doi.org/10.1109/TC.2023.3343094)"
        )
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('en/publication.md')
update_file('zh/publication.md')
