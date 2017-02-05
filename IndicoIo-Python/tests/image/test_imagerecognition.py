#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from indicoio import image_recognition
from .indico_image_base import ImageTest, DIR

class ImageRecognitionTest(ImageTest):

    def test_single_image_recognition(self):
        test_data = os.path.normpath(os.path.join(DIR, "data", "fear.png"))
        response = image_recognition(test_data, api_key = self.api_key, top_n=3)
        self.assertIsInstance(response, dict)
        self.assertEqual(len(response), 3)
        self.assertIsInstance(list(response.values())[0], float)

    def test_batch_image_recognition(self):
        test_data = os.path.normpath(os.path.join(DIR, "data", "fear.png"))
        response = image_recognition([test_data, test_data], api_key = self.api_key, top_n=3)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response[0]), 3)
        self.assertIsInstance(list(response[0].values())[0], float)

    def test_expected_response(self):
        test_data = os.path.normpath(os.path.join(DIR, "data", "keyboard.jpg"))
        response = image_recognition(test_data, api_key = self.api_key, top_n=3)
        assert "space bar" in response.keys()
