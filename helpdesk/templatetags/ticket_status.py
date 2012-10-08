from django.utils.translation import ugettext_lazy as _, ugettext
from django import template

from helpdesk.models import Ticket

register = template.Library()

@register.simple_tag
def get_html_ticket_status(status):
    res = ''

    status_ops = {'1': [Ticket.RESOLVED_STATUS, Ticket.CLOSED_STATUS, Ticket.DUPLICATE_STATUS],
                  '2': [Ticket.RESOLVED_STATUS, Ticket.CLOSED_STATUS, Ticket.DUPLICATE_STATUS],
                  '3': [Ticket.CLOSED_STATUS, Ticket.DUPLICATE_STATUS],
                  '4': [Ticket.REOPENED_STATUS, Ticket.DUPLICATE_STATUS],
                  '5': [Ticket.RESOLVED_STATUS, Ticket.CLOSED_STATUS, Ticket.OPEN_STATUS],
                 }
    label_vals = {'1': 'Abierto', '2': 'Reabierto', '3': 'Resuelto', '4': 'Cerrado',
                  '5': 'Duplicado'}
    ticket_status = status_ops[str(status)]
    for st in ticket_status:
        res += '<label class="checkbox inline active"><input type="radio" name="new_status"  value="{0}">{1}</label>'.format(st, label_vals[str(st)])
    return res
