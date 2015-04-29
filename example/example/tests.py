from django.test import TestCase
from django.core.management import execute_from_command_line


class ViewsTestCase(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_sum(self):
        resp = self.client.get('/')
        
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, b'3')

