#!/usr/bin/python
# -*- coding: utf-8 -*-
from indicoio import twitter_engagement
from .indico_text_base import TextTest

class TwitterEngagementTest(TextTest):

    def test_twitter_engagement(self):
        test_string = "Worst song ever."
        response = twitter_engagement(test_string)

        self.assertIsInstance(response, float)
        self.assertTrue(response <= 1)
        self.assertTrue(response >= 0)

    def test_batch_twitter_engagement(self):
        test_string = "Worst song ever."
        response = twitter_engagement([test_string, test_string])

        self.assertTrue(isinstance(response, list))
        self.assertIsInstance(response[0], float)
        self.assertEqual(response[0], response[1])
