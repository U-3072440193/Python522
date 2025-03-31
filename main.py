import os

dirs = [r'Work\F1', r'Work\F2\F21']

for d in dirs:
    os.makedirs(d)

files = {
    'Work': ['w.txt'],
    r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
    r'Work\F2\F21': ['f211.txt', 'f212.txt']
}

for key, value in files.items():
    for file in value:
        file_path = os.path.join(key, file)
        open(file_path, 'w').close()
