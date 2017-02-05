# -*- coding: utf-8 -*-
from indicoio import keywords
from .indico_text_base import TextTest

class KeywordsTest(TextTest):

    def test_batch_keywords_v1(self):
        test_data = ["A working api is key to the success of our young company"]
        words = [set(text.lower().split()) for text in test_data]
        response = keywords(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(set(response[0].keys()).issubset(words[0]))

    def test_keywords_language_detect_v1(self):
        text = "il a remporté sa première victoire dans la descente de Val Gardena en Italie"
        words = set(text.lower().split())

        results = keywords(text, language = 'detect')
        self.assertTrue(set(results.keys()).issubset(words))

        results = keywords(text, top_n=3)
        assert len(results) is 3

        results = keywords(text, threshold=.1)
        for v in results.values():
            assert v >= .1

    def test_keywords_language_v1(self):
        text = "il a remporté sa première victoire dans la descente de Val Gardena en Italie"
        words = set(text.lower().split())

        results = keywords(text, language = 'French')
        self.assertTrue(set(results.keys()).issubset(words))

        results = keywords(text, top_n=3)
        assert len(results) is 3

        results = keywords(text, threshold=.1)
        for v in results.values():
            assert v >= .1

    def test_keywords_v1(self):
        text = "A working api is key to the success of our young company"
        words = set(text.lower().split())

        results = keywords(text)
        sorted_results = sorted(results.keys(), key=lambda x:results.get(x), reverse=True)
        assert 'api' in sorted_results[:3]
        self.assertTrue(set(results.keys()).issubset(words))

        results = keywords(text, top_n=3)
        assert len(results) is 3

        results = keywords(text, threshold=.1)
        for v in results.values():
            assert v >= .1

    def test_keywords_v2(self):
        test_data = "A working api is key to the success of our young company"
        response = keywords(test_data, version=2)
        self.assertTrue(isinstance(response, dict))
        self.assertTrue(all([key in test_data for key in response.keys()]))

    def test_batch_keywords_v2(self):
        test_data = ["A working api is key to the success of our young company"]
        response = keywords(test_data, version=2)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(all([key in test_data[0] for key in response[0].keys()]))
