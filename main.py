# from parsers import Parser
#
#
# def main():
#     pars = Parser('https://www.ixbt.com/live/index/news/', 'new.txt')
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# from jinja2 import Template

# name = "Nigga"
# age = 22

# per = {'name': "Niggor", 'age': 41}
# tm = Template("sup am {{p.age}} yo, maname {{p['name'].upper()}}")
# msg = tm.render(p=per)
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# per = Person('niggor', 44)
#
# tm = Template("sup am {{p.age}} yo, maname {{p.get_name().upper()}}")
# msg = tm.render(p=per)
# print(msg)
# cities = [
#     {'id': 1, 'city': 'Moscow'},
#     {'id': 2, 'city': 'Oslo'},
#     {'id': 3, 'city': 'Minsk'},
#     {'id': 4, 'city': 'Cornwall'},
# ]
# link = """
# <select>
# {% for c in cities %}
#     {% if c.id > 3 %}
#         <option value="{{ c['id'] }}">{{ c.city }}</option>
#     {%elif c.city =='Moscow'%}
#         {{c.city}}
#     {% else%}
#         <option>{{c.city}}</option>
#     {% endif %}
# {% endfor %}
# </select>
# """
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)
#
# cars = [
#     {'model': 'Audi', 'price': 325666},
#     {'model': 'Opel', 'price': 122245},
#     {'model': 'BMV', 'price': 32000},
#     {'model': 'Subaru', 'price': 215666},
# ]
#
# tpl = "{{cs|sum(attribute='price')}}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# html = """
# {% macro input_func(name, value='', type='text', size=20) %}
# <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ input_func('username','21') }}</p>
# <p>{{ input_func('email') }}</p>
# <p>{{ input_func('pass') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

from jinja2 import Environment, FileSystemLoader

# person = [
#     {'name': "Alex"},
#     {'name': "Nick"},
#     {'name': "Vasil", }
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template("index.html")
# msg = tm.render(users=person, title="About jojo")
#
# print(msg)


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template("about.html")
msg = tm.render()

print(msg)

