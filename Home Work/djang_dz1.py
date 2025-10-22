from jinja2 import Template

names = [
    {'href': '/index', 'name': 'Главная'},
    {'href': '/news', 'name': 'Новости'},
    {'href': '/about', 'name': 'О нашей компании'},  # исправлены кавычки
    {'href': '/shop', 'name': 'Магазин'},
    {'href': '/contacts', 'name': 'Контакты'},
]
# Задача 1
link = """
<ul>
    {% for c in names %}
        {% if c.href == '/index' %} {# исправлено = на == #}
            <li><a href="{{ c.href }}" class="active">{{ c.name }}</a></li>
        {% else %}
            <li><a href="{{ c.href }}">{{ c.name }}</a></li>
        {% endif %}
    {% endfor %}
</ul>
"""

# tm = Template(link)
# msg = tm.render(names=names)
# print(msg)

# Задача 2

input_ = """
{% macro input_func( name, placeholder,type='text') %}
<input type="{{ type }}" name="{{ name }}" placeholder="{{placeholder}}">
{% endmacro %}
<p>{{ input_func('firstname','Имя') }}</p>
<p>{{ input_func('lasname','Фамилия') }}</p>
<p>{{ input_func('adress','Адрес') }}</p>
<p>{{ input_func('phone','Телефон','tel') }}</p>
<p>{{ input_func('email','Почта','email') }}</p>
"""

tm = Template(input_)
msg = tm.render()
print(msg)
