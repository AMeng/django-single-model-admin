from django.contrib.auth.models import User
from django.test import Client, TestCase
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

from app.models import TestModel


class AbstractTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser('user', 'email@test.com', 'password')
        self.client = Client()
        self.client.login(username='user', password='password')

    def assertMessage(self, response, message):
        messages = [m.message for m in response.context['messages']]
        error_text = 'Message "{0}" not found. Messages: {1}'.format(message,
                                                                     messages)
        self.assertTrue(message in messages, error_text)


class NoObjectsTestCase(AbstractTestCase):

    def test_can_add_new_model(self):
        response = self.client.get(reverse('admin:app_testmodel_add'),
                                   follow=True)
        self.assertEqual(response.status_code, 200)

    def test_changelist_redirects_to_add(self):
        response = self.client.get(reverse('admin:app_testmodel_changelist'),
                                   follow=True)
        self.assertRedirects(response, reverse('admin:app_testmodel_add'))

    def test_renders_add_button(self):
        response = self.client.get(reverse('admin:app_list', args=['app']),
                                   follow=True)
        self.assertContains(
            response,
            '<a href="/admin/app/testmodel/add/" class="addlink">Add</a>',
            html=True)


class SingleObjectTestCase(AbstractTestCase):

    def setUp(self):
        super(SingleObjectTestCase, self).setUp()
        TestModel.objects.create(field='value')

    def test_cannot_add_new_model(self):
        response = self.client.get(reverse('admin:app_testmodel_add'),
                                   follow=True)
        self.assertRedirects(response,
                             reverse('admin:app_testmodel_change', args=[1]))
        self.assertMessage(
            response,
            'Do not add additional instances of testmodel. Only one is needed.'
            )

    def test_cannot_see_changelist(self):
        response = self.client.get(reverse('admin:app_testmodel_changelist'),
                                   follow=True)
        self.assertRedirects(response,
                             reverse('admin:app_testmodel_change', args=[1]))

    def test_does_not_render_add_button(self):
        response = self.client.get(reverse('admin:app_list', args=['app']),
                                   follow=True)
        self.assertNotContains(
            response,
            '<a href="/admin/app/testmodel/add/" class="addlink">Add</a>',
            html=True)


class MultipleObjectsTestCase(AbstractTestCase):

    def setUp(self):
        super(MultipleObjectsTestCase, self).setUp()
        TestModel.objects.create(field='value1')
        TestModel.objects.create(field='value2')
        TestModel.objects.create(field='value3')

    def test_cannot_add_new_model(self):
        response = self.client.get(reverse('admin:app_testmodel_add'),
                                   follow=True)
        self.assertRedirects(response,
                             reverse('admin:app_testmodel_changelist'))
        self.assertMessage(
            response,
            'Do not add additional instances of testmodel. Only one is needed.'
            )

    def test_can_see_changelist(self):
        response = self.client.get(reverse('admin:app_testmodel_changelist'),
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertMessage(
            response,
            ('There are multiple instances of testmodel. There should only be '
             'one.'))

    def test_does_not_render_add_button(self):
        response = self.client.get(reverse('admin:app_list', args=['app']),
                                   follow=True)
        self.assertNotContains(
            response,
            '<a href="/admin/app/testmodel/add/" class="addlink">Add</a>',
            html=True)
