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
        self.queue_main.save()
        # Creating 'urgent' queue
        self.queue_urg = milkman.deliver(Queue)
        self.queue_urg.title = 'Urgent'
        self.queue_urg.slug = 'urg'
        self.queue_urg.save()
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
        # Creating a simple Ticket
        self.ticket = milkman.deliver(Ticket)
        # HTTP client
        self.client = Client()

    def tearDown(self):
        self.user.delete()
        self.staff_user.delete()
        self.queue_main.delete()
        self.queue_urg.delete()
        self.ticket.delete()

    def test_user_create_ticket(self):
        self.client.login(username=self.user.username, password=PASSWORD)
        post_data = {'title': 'First ticket title',
                     'queue': self.queue_main.id,
                     'submitter_email': self.user.email,
                     'body': 'First ticket body',
                     'priority': 3,
                     }
        response = self.client.post(reverse('helpdesk_home'),
                                    post_data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template[0].name,
                         'helpdesk/public_view_ticket.html')
        ticket = Ticket.objects.get(title=post_data['title'])
        self.assertEqual(ticket.title, post_data['title'])
        self.assertEqual(ticket.queue.id, post_data['queue'])
        self.assertEqual(ticket.submitter_email, post_data['submitter_email'])
        self.assertEqual(ticket.description, post_data['body'])
        self.assertEqual(ticket.priority, post_data['priority'])

    def test_staff_user_create_ticket(self):
        self.client.login(username=self.staff_user.username, password=PASSWORD)
        post_data = {'title': 'Staff ticket title',
                     'queue': self.queue_main.id,
                     'submitter_email': self.user.email,
                     'body': 'Staff ticket body',
                     'priority': 3,
                     }
        response = self.client.post(reverse('helpdesk_submit'),
                                    post_data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template[0].name, 'helpdesk/ticket.html')
        ticket = Ticket.objects.get(title=post_data['title'])
        self.assertEqual(ticket.title, post_data['title'])
        self.assertEqual(ticket.queue.id, post_data['queue'])
        self.assertEqual(ticket.submitter_email, post_data['submitter_email'])
        self.assertEqual(ticket.description, post_data['body'])
        self.assertEqual(ticket.priority, post_data['priority'])

    def test_staff_main_page_is_dashboard(self):
        self.client.login(username=self.staff_user.username, password=PASSWORD)
        response = self.client.get(reverse('helpdesk_home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template[0].name, 'helpdesk/dashboard.html')

    def test_user_cannot_create_non_public_ticket(self):
        post_data = {'title': 'First ticket title',
                     'queue': self.queue_main.id,
                     'submitter_email': self.user.email,
                     'body': 'First ticket body',
                     'priority': 3,
                     }

        self.client.login(username=self.user.username, password=PASSWORD)
        response = self.client.post(reverse('helpdesk_submit'),
                                    post_data,
                                    follow=True)

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_acces_to_ticket(self):
        self.client.login(username=self.user.username, password=PASSWORD)
        response = self.client.get(reverse('helpdesk_view', args=[self.ticket.id]))
        self.assertEqual(response.status_code, 404)

    def test_ticket_assign(self):
        t = Ticket.objects.get(id=self.ticket.id)
        self.assertEqual(t.assigned_to, None)
        t.assigned_to = self.staff_user
        t.save()
        t_assigned = Ticket.objects.get(id=self.ticket.id)
        self.assertEqual(t_assigned.assigned_to, self.staff_user)

