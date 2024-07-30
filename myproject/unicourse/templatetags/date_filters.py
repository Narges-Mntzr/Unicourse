from django import template
from datetime import datetime

register = template.Library()


@register.filter
def is_class_today(course_days):
    today = datetime.today().strftime("%A")
    print(today)
    return today in course_days
