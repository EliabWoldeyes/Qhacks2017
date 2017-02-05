import os

from indicoio import summarization
from .indico_text_base import TextTest, DIR

TEXT_DATA = open(os.path.join(DIR, "data", "long_text.txt"), 'rb').read()

class SummarizationTest(TextTest):

    def test_summarization(self):
        response = summarization(TEXT_DATA, top_n=5)
        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 5)
