from dateutil import parser
from django import template

register = template.Library()


@register.filter
def format_string_date(date, fmt=None):
    """Format a date string or datetime object"""
    if date is None:
        return ""

    # If it's already a datetime object, use it directly
    if hasattr(date, "strftime"):
        if not fmt:
            fmt = "%Y-%m-%d"
        return date.strftime(fmt)

    # If it's a string, parse it first
    try:
        parsed_date = parser.parse(str(date))
        native = parsed_date.replace(tzinfo=None)
        if not fmt:
            fmt = "%Y-%m-%d"
        return native.strftime(fmt)
    except (ValueError, TypeError):
        return str(date)
