#!/usr/bin/python
# -*- coding: utf-8 -*-


from indicoio import sentiment_hq
from .indico_text_base import TextTest

class SentimentHQTest(TextTest):

    def test_batch_sentiment_hq(self):
        test_data = ['Worst song ever', 'Best song ever']
        response = sentiment_hq(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(response[0] < 0.5)

    def test_sentiment_hq(self):
        test_string = "Worst song ever."
        response = sentiment_hq(test_string)

        self.assertTrue(isinstance(response, float))
        self.assertTrue(response < 0.5)

        test_string = "Best song ever."
        response = sentiment_hq(test_string)
        self.assertTrue(isinstance(response, float))
        self.assertTrue(response > 0.5)
