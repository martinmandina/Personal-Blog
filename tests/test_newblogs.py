import unittest
from app import db
from app.models import User,BlogPost


class BlogMOdelTest(unittest.TestCase):
   def setUp(self):
       self.user_john = User(username = 'john',password = 'johnjohn')
       self.new_blog = Blog(content='johnjohnjohn')

   def test_check_instance_variable(self):
       self.assertEquals(self.new_blog.content,'johnjohnjohn')



