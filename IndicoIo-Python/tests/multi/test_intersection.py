from indicoio import intersections, IndicoError
from .indico_multi_base import MultiTest

class IntersectionTest(MultiTest):

    def test_intersections_not_enough_data(self):
        test_data = ['test_Data']
        self.assertRaises(
            IndicoError,
            intersections,
            test_data,
            apis=['text_tags', 'sentiment']
        )

    def test_intersections_wrong_number_of_apis(self):
        test_data = ['test data']*3
        self.assertRaises(
            IndicoError,
            intersections,
            test_data,
            apis=['text_tags', 'sentiment', 'language']
        )

    def test_intersections_bad_api_type(self):
        test_data = ['test data']*3
        self.assertRaises(
            IndicoError,
            intersections,
            test_data,
            apis=['text_tags', 'fer']
        )

    def test_intersections_valid_input(self):
        test_data = ['test data']*3
        apis = ['text_tags', 'sentiment']
        results = intersections(test_data, apis=apis)
        assert set(results.keys()) < set(apis)

    def test_intersections_valid_raw_input(self):
        test_data = {
            'sentiment': [0.1, 0.2, 0.3],
            'twitter_engagement': [0.1, 0.2, 0.3]
        }
        results = intersections(test_data, apis=['sentiment', 'twitter_engagement'])
        assert set(results.keys()) < set(test_data.keys())
