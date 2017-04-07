from django.contrib.auth.models import User

from django.test import TestCase
from .models import user, calender, User_signup
# class SimpleTest(TestCase):
class login(object):
    print "hello"
    def __init__(self, testcase, user, password):

        self.testcase = testcase
        success = testcase.client.login(username=user, password=password)
        self.testcase.assertTrue(
            success,
            "login with username=%r, password=%r failed" % (user, password)
        )
    def __enter__(self):
        print "fdsf"
        pass

    def __exit__(self, *args):
        self.testcase.client.logout()

#     def test_basic(self):
#         """
#         this is simple test case
#         """
#         resp = self.client.get('/')
#         self.user = User.objects.create_user(username='u@tudip.nl', password='tudip123')
#         login = self.client.login(username='u@tudip.nl', password='tudip123')
#         print "login", login
#         self.assertEqual(resp.status_code, 200)
#         self.assertTrue(login)
#         self.assertTrue(resp)
#
# class Mytest(TestCase):
#
#     def signup(self):
#         resp = self.client.get('/')
#         print "helllo",resp




