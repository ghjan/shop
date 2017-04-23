import unittest
from django.core.mail import EmailMessage
from django.conf import settings

from .tasks import order_created, send_email_message


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_send_mail_simple(self):
        # create invoice e-mail
        subject = 'Test mail from django'
        message = 'just a test mail from django.'
        email = EmailMessage(subject, message, settings.MAIL_ADMIN, [settings.MAIL_ADMIN, settings.MAIL_TEST])

        # send e-mail
        email.send()

    def test_task_send_mail(self):
        subject = 'Test mail from django'
        content = 'just a test mail from django.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to = [settings.DEFAULT_FROM_EMAIL, settings.MAIL_TEST]
        send_email_message.delay(subject, content, from_email, to)


if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
