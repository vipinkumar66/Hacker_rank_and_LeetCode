x= "aaabcdef"
value = ""
for y in x:
    if y != value:
        value += y
print(value)