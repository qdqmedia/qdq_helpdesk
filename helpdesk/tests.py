from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from milkman.dairy import milkman

from helpdesk.models import Queue, Ticket

PASSWORD = '1234'


class TicketsTestCase(TestCase):
    def setUp(self):
        # Creating 'main' queue
        self.queue_main = milkman.deliver(Queue)
        self.queue_main.title = 'Main'
        self.queue_main.slug = 'main'
        self.queue_main.allow_public_submission = True
        # Creating 'urgent' queue
        self.queue_urg = milkman.deliver(Queue)
        self.queue_urg.title = 'Urgent'
        self.queue_urg.slug = 'urg'
        # Creating a regular user
        self.user = milkman.deliver(User)
        self.user.set_password(PASSWORD)
        self.user.email = 'email1@email.com'
        self.user.save()
        # Creating a staff user
        self.staff_user = milkman.deliver(User)
        self.staff_user.is_staff = True
        self.staff_user.set_password(PASSWORD)
        self.staff_user.email = 'email2@email.com'
        self.staff_user.save()
        # HTTP client
        self.client = Client()

    def tearDown(self):
        self.user.delete()
        self.staff_user.delete()

    def test_user_create_ticket(self):
        post_data = {'title': 'First ticket title',
                     'queue': self.queue_main.id,
                     'submitter_email': self.user.email,
                     'body': 'First ticket body',
                     'priority': 3,
                     }
        self.client.login(username=self.user.username, password=PASSWORD)
        response = self.client.post(reverse('helpdesk_home'), post_data)
        import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template[0].name, 'helpdesk/public_homepage.html')
        ticket = Ticket.objects.get(title=post_data['ticket'])
        import ipdb; ipdb.set_trace()

    def test_staff_user_create_ticket(self):
        pass
