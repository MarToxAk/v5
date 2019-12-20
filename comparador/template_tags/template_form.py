from django import template
register = template.Library()


@register.filter(name='add_attr')
def add_attr(field):
    attrs = {'class': 'teste'}


    return field.as_widget(attrs=attrs)
