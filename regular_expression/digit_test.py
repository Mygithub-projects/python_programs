import re

sentence = "I have 560 computer books and 284 physics books."


ans = re.findall(r"\d{1}",sentence)
print(ans)
