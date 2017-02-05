import os

from indicoio import analyze_image
from indicoio.image import IMAGE_APIS
from .indico_multi_base import MultiTest

DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "image")

class AnalyzeImageTest(MultiTest):

    def test_multi_api_image(self):
        test_data = os.path.normpath(os.path.join(DIR, "data/48by48.png"))
        response = analyze_image(test_data, apis=IMAGE_APIS.keys())

        self.assertTrue(isinstance(response, dict))
        self.assertTrue(set(response.keys()) == set(IMAGE_APIS.keys()))

    def test_batch_multi_api_image(self):
        test_data = [os.path.normpath(os.path.join(DIR, "data/48by48.png")),
                     os.path.normpath(os.path.join(DIR, "data/48by48.png"))]
        response = analyze_image(test_data, apis=IMAGE_APIS.keys())
        self.assertTrue(isinstance(response, dict))
        self.assertTrue(set(response.keys()) == set(IMAGE_APIS.keys()))
        self.assertTrue(isinstance(response["fer"], list))
