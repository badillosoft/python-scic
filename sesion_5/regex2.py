import re

text = input("Escribe un mensaje: ")

pattern = "([\w\.\-\_]+)@(\w+)(\.\w{2,3}){1,2}"

text_mod = ""

for m in re.finditer(pattern, text):
    user = m.group(1)
    i = m.start(1)
    j = i + len(user)
    text_mod = text[0:i] + "*" * len(user) + text[j:]

print(text_mod)