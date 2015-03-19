from django.core.mail import send_mail

from django.conf import settings

if not settings.configured:
    settings.configure(DEBUG=True)

send_mail('Subject here', 'Here is the message.', 'from@example.com',
    ['lykhenko.olexandr@gmail.com'], fail_silently=False)