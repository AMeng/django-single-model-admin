from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from app.models import TestModel


class AbstractTestCase(TestCase):
    def setUp(self):
        TestModel.objects.all().delete()
        User.objects.create_superuser('user', 'email@test.com', 'password')
        self.client = Client()
        self.client.login(username='user', password='password')


class NoObjectsTestCase(AbstractTestCase):

    def test_can_add_new_model(self):
        response = self.client.get(reverse('admin:app_testmodel_add'))
        self.assertEqual(response.status_code, 200)

    def test_changelist_redirects_to_add(self):
        response = self.client.get(reverse('admin:app_testmodel_changelist'))
        self.assertRedirects(response, 'http://testserver/admin/app/testmodel/add/')

    def test_renders_add_button(self):
        response = self.client.get(reverse('admin:app_list', args=['app']))
        self.assertContains(response, '<a href="/admin/app/testmodel/add/" class="addlink">Add</a>', html=True)


class SingleObjectTestCase(AbstractTestCase):

    def setUp(self):
        super(SingleObjectTestCase, self).setUp()
        TestModel.objects.create(field='value')

    def test_cannot_add_new_model(self):
        response = self.client.get(reverse('admin:app_testmodel_add'), follow=True)
        self.assertRedirects(response, 'http://testserver/admin/app/testmodel/1/')

    def test_cannot_see_changelist(self):
        response = self.client.get(reverse('admin:app_testmodel_changelist'))
        self.assertRedirects(response, 'http://testserver/admin/app/testmodel/1/')

    def test_does_not_render_add_button(self):
        response = self.client.get(reverse('admin:app_list', args=['app']))
        self.assertNotContains(response, '<a href="/admin/app/testmodel/add/" class="addlink">Add</a>', html=True)


class MultipleObjectsTestCase(AbstractTestCase):

    def setUp(self):
        super(MultipleObjectsTestCase, self).setUp()
        TestModel.objects.create(field='value1')
        TestModel.objects.create(field='value2')
        TestModel.objects.create(field='value3')

    def test_cannot_add_new_model(self):
        response = self.client.get(reverse('admin:app_testmodel_add'))
        self.assertRedirects(response, 'http://testserver/admin/app/testmodel/')

    def test_can_see_changelist(self):
        response = self.client.get(reverse('admin:app_testmodel_changelist'))
        self.assertEqual(response.status_code, 200)

    def test_does_not_render_add_button(self):
        response = self.client.get(reverse('admin:app_list', args=['app']))
        self.assertNotContains(response, '<a href="/admin/app/testmodel/add/" class="addlink">Add</a>', html=True)
