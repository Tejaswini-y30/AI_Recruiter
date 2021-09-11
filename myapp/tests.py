from django.test import TestCase , SimpleTestCase
from django.urls import resolve, reverse
from myapp.views import index,form_submitted,msg,msg1,msg2,admin

class TestUrls(SimpleTestCase):
    def test_home_urls_is_resolved(self):
        assert 1==1
        url = reverse('index.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func,index)


    
# Create your tests here.
#