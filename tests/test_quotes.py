import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    
    def setUp(self):
       
        self.new_quote = Quote(Ovidiu platon,11,"I don’t care if it works on your machine! We are not shipping your machine!","http://quotes.stormconsultancy.co.uk/quotes/11")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))