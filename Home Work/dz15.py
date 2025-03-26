print("Домашнее задание")
s = "I am learning Python. hello, WORLD!"
print(s[:s.find("h")] + s[s.rfind("h"):s.find("h"):-1] + s[s.rfind("h"):])
