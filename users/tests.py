from django.contrib.auth import get_user
from django.urls import reverse


from django.contrib.auth.models import User
from django.test import TestCase



# Create your tests here.
#
# class RegistrationTestCase(TestCase):
#     def test_user_account_is_created(self):
#         response=self.client.post(
#             reverse('users:register'),
#         data={
#             'username': 'asu1234',
#             'first_name': 'asu12',
#             'last_name': 'Ataxanova',
#             'email': 'asu123@gmail.com',
#             'password': 'asu12345678'
#         }
#         )
#         user=User.objects.get(username="asu1234")
#         self.assertEqual(user.username, 'asu1234')
#         self.assertEqual(user.first_name, 'asu12')
#         self.assertEqual(user.last_name, 'Ataxanova')
#         self.assertEqual(user.email, 'asu123@gmail.com')
#         self.assertNotEqual(user.password, 'some_password')
#
#     def test_required_fields(self):
#         response=self.client.post(
#             reverse('users:register'),
#             data={
#                 'username': 'asu1',
#                 'first_name': 'asu1',
#                 'last_name': 'asu11',
#                 'email': 'asu1@gmail.com',
#                 'password': 'asuasu11',
#             }
#             )
#         user_count=User.objects.count()
#         self.assertEqual(user_count, 0)
#         self.assertFormError(response, 'form', 'username', 'This field is required.')
#
#     def test_invalid_email(self):
#         response=self.client.post(
#             reverse('users:register'),
#             data={
#                 'username': 'asu4',
#                 'first_name': 'asu4',
#                 'last_name': 'Ataxanova',
#                 'email': 'invalid email'
#             }
#         )
#         user_count=User.objects.count()
#         self.assertEqual(user_count, 0)
#         self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
#
#     def test_unique_username(self):
#         # 1.create a user
#         user = User.objects.create_user(username='mirko1', first_name='mirko1')
#         user.set_password('somepass')
#         user.save()
#
# #         2.try to create a another user with that same username
#         response = self.client.post(
#             reverse('users:register'),
#             data={
#                 'username': 'mirko1',
#                 'first_name': 'mirko1',
#                 'last_name': 'mirko1',
#                 'email': 'mirko11@gmail.com',
#                 'password': 'mirko98765',
#             })
#         #     3.check that the second user was not created
#         user_count = User.objects.count()
#         self.assertEqual(user_count, 1)
#
#         # 4. check tat the form contains the error message
#         self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')



class LoginTestCase(TestCase):
    def test_successful_login(self):
        db_user = User.objects.create(username='test', first_name='test')
        db_user.set_password('somepass')
        db_user.save()

        self.client.post(
            reverse('users:login'),
            data={
                'username': 'test',
                'password': 'somepass'
            }
        )
        user = get_user(self.client)
        self.assertEqual(user.is_authenticated,True)

