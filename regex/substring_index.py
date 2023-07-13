# FIRST METHOD

import regex

string = "aaabaa"
substring = "aa"

pattern = regex.compile(substring)
matches = pattern.finditer(string,overlapped=True)

for match in matches:
    start_index = match.start()
    end_index = match.end()
    print(f"Substring '{substring}' found from index {start_index} to {end_index-1}")


# SECOND METHOD

import re

full_string = input()
to_find = input()

pattern = re.compile(f"(?={to_find})")

match = pattern.finditer(full_string)
found = False

for m in match:
    print((m.start(), m.end() + len(to_find) - 1))
    found = True

if not found:
    print((-1, -1))

