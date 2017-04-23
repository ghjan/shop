from celery import task
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage as DjangoEmailMessage, get_connection
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name,
                                                                                               order.id)
    mail_sent = send_mail(subject, message, settings.MAIL_ADMIN, [order.email])
    return mail_sent


@task
def send_email_message(subject, content, from_email, to):
    '''
    function: 异步发送email消息

    message_id - email消息id
    '''

    # connection = get_connection(backend='common.core.mail.backends.PublicEmailBackend')
    to_ = to if type(to) in (list, tuple, set) else [to, ]
    email = DjangoEmailMessage(subject=subject,
                               body=content,
                               from_email=from_email,
                               to=to_,
                               # connection=connection,
                               headers={'From': 'Myshop <%s>' % settings.EMAIL_HOST_USER})
    # email.content_subtype = 'html'

    sended_count = email.send()
    if sended_count > 0:
        return True
    else:
        return False
