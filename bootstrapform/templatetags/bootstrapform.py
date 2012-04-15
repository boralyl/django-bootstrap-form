import re

from django import template
from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe

register = template.Library()

FORM_ELEMENT_RE = re.compile(r'(<(input|textarea|select)\s)')


@register.filter
def bootstrapform(element, css_class=""):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        template = get_template("bootstrapform/field.html")
        context = Context({'field': element, 'css_class': css_class})
    else:
        template = get_template("bootstrapform/form.html")
        context = Context({'form': element, 'css_class': css_class})

    return template.render(context)


@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"


@register.filter
def add_class(value, css_class):
    """
    Adds a css class to any input, textarea, or select elements
    """
    string = unicode(value)
    match = FORM_ELEMENT_RE.search(string)
    css_class = "class='%s' " % (css_class, )

    if match:
        return mark_safe(string.replace(match.group(),
            match.group() + css_class))
    return value
