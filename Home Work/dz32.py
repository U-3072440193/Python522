import requests
import json
import csv

url = "https://jsonplaceholder.typicode.com/todos"
filename = "convert_json_to_csv.json"

response = requests.get(url)
todos = json.loads(response.text)
print(todos)


class JsonConverter:
    @staticmethod
    def load(file_name):
        try:
            data = json.load(open(file_name, encoding="utf-8"))
        except FileNotFoundError:
            data = {}
        finally:
            return data

    @staticmethod
    def add_to_json(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(todos, f, indent=2, ensure_ascii=False)

    @staticmethod
    def add_to_csv(file_name):
        data = JsonConverter.load(file_name)
        with open("convert_json_to_csv.csv", "w") as f:
            writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=data[0].keys())
            writer.writeheader()
            for d in data:
                writer.writerow(d)


JsonConverter.add_to_json(filename)
JsonConverter.add_to_csv(filename)
