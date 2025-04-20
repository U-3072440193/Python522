class Student:
    def __init__(self, name):
        self.name = name

    def display(self, model, cpu, ram):
        self.notebook = self.Notebook_info(model, cpu, ram)
        return f"{self.name} => {self.notebook.model}, {self.notebook.cpu}, {self.notebook.ram}"

    class Notebook_info:
        def __init__(self, model, cpu, ram):
            self.model = model
            self.cpu = cpu
            self.ram = ram


roman = Student("Roman")
inner = roman.display("HP", "i7", "16")
print(inner)

vladimir = Student("Vladimir")
inner = vladimir.display("HP", "i7", "16")
print(inner)
