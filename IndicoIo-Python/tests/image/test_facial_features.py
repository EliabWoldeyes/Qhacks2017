#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from indicoio import facial_features
from .indico_image_base import ImageTest, DIR

class FacialFeaturesTest(ImageTest):

    def test_batch_facial_features(self):
        test_data = [os.path.normpath(os.path.join(DIR, "data/48by48.png"))]
        response = facial_features(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], list))
        self.assertEqual(len(response[0]), 48)

    def test_good_facial_features(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/48by48.png"))
        response = facial_features(test_face)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 48)
        self.check_range(response)

    def test_rgba_int_array_facial_features(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/48by48rgba.png"))
        response = facial_features(test_face)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 48)
        self.check_range(response)

    def test_good_int_array_facial_features(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/48by48.png"))
        response = facial_features(test_face)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 48)
        self.check_range(response)
