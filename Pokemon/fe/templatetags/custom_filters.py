from django import template

register = template.Library()


@register.filter
def dash_to_space(value):
    return value.replace("-", " ")


@register.filter
def extract_id_from_url(value, arg):
    if arg == "pokemon":
        return value[34:-1]
    elif arg == "move":
        return value[31:-1]
    elif arg == "type":
        return value[31:-1]
