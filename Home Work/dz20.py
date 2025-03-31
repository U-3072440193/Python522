import os


print("Домашнее задание")
empty_files_dir = "Work/empty_files"
os.makedirs(empty_files_dir)


def empty_file_search(directory):
    for root, directories, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                if size == 0:
                    new_file_path = os.path.join(empty_files_dir, file)
                    os.rename(file_path, new_file_path)
                    print(f"Файл {file} перемещён из {file_path} в {new_file_path}")
                else:
                    print(f"{file_path} - {size} bytes")


empty_file_search("Work")
