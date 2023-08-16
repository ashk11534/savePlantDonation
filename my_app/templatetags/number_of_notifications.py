
from django import template
from ..models import User, UserNotification

register = template.Library()

@register.filter
def total_notifications(user_id):
    receiver = User.objects.get(id=user_id)
    notifications = UserNotification.objects.filter(receiver=receiver, is_active=True)
    return len(notifications)
