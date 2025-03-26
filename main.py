
word = "Minas"  # Искомое слово
with open(r"C:\Program Files (x86)\R.G. Catalyst\Medieval 2 - Total War Kingdoms\mods\Third_Age_3\data\world\maps\base\descr_regions.txt", "r", encoding="utf-8") as f:
    for line in f:
        if word in line:
            print(line.strip())  # Вывод найденной строк