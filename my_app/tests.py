from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

# Create your tests here.

class TaskListTest(TestCase):
    
    def setUp(self):
        """
        This runs before every test. 
        We create a dummuy user and a task to test with.
        """
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.task = Task.objects.create(user=self.user, title='Test Task', description='Testing...')

    def test_task_list_accessible_by_logged_in_user(self):
        """Check if a logged in user can see the task list."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_task_list_redirects_anonymous_user(self):
        """Check id a logged out user is redirected to login."""
        response = self.client.get(reverse('task_list'))
        # 302 is the status code for a redirect
        self.assertEqual(response.status_code, 302)

    def test_user_can_only_see_their_task(self):
        """The test ensure that User A cannot see the user B tasks."""
        #Create a second dummy user .
        other_user = User.objects.create_user(username='otheruser', password='password123')
        Task.objects.create(user=other_user, title='secret Task')

        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('task_list'))

        self.assertContains(response, 'Test Task')
        self.assertNotContains(response, 'secret Task')