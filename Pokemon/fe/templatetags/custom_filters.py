from django import template

register = template.Library()


@register.filter
def dash_to_space(value):
    return value.replace("-", " ")


@register.filter
def extract_id_from_url(value, arg):
    if arg == "pokemon":
        return value[34:-1]
