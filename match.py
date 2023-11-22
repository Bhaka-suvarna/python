import re
matcher = re.finditer("a{2}", "ababaabaaaabaaabababaaabdbaab")
for match in matcher:
    print(match.start(), '   ', match.group())