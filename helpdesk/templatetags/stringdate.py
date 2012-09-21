from datetime import datetime

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def string_to_date(val):
    # Don't take care about decimals for seconds
    format_val = val[0:19]
    date_obj = datetime.strptime(format_val, '%Y-%m-%d %H:%M:%S')
    return date_obj
