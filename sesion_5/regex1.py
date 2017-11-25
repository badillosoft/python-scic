import re

pattern = "([\w\.\-\_]+)@(\w+)(\.\w{2,3}){1,2}"

text = "Mi correo es ana@@gmail.com y el tuyo es pepe@hotmail.com"

for m in re.finditer(pattern, text):
    print(m.group(0))
    print(m.start(0))
    print(m.start(0) + len(m.group(0)) - 1)