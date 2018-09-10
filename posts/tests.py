from django.test import TestCase
# Create your tests here.
from .models import Post
class PostModelTest(TestCase):
	"""docstring for PostModelTest"""
	def setup(self):
		Post.objects.Create(text='just a test case')
	def test_text_content(self):
		post=Post.objects.get(id=1)
		expected_object_name=f'{post.text}'
		self.assertEqual(expected_object_name,'just a test case')