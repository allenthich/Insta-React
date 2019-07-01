from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

class TMdbTests(APITestCase):
    def __init__(self, *args, **kwargs):
        super(TMdbTests, self).__init__(*args, **kwargs)
        self.api_title_url = reverse('api-title')

    def test_get_title_200(self):
        """
        Ensure we can retrieve an appropriate title object
        """
        response = self.client.get(self.api_title_url + "?query=breaking+bad")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictContainsSubset({
            "page": 1,
            "total_results": 1,
            "total_pages": 1,
            "results": [
                {
                    "original_name": "Breaking Bad",
                    "genre_ids": [
                        18
                    ],
                    "name": "Breaking Bad",
                    "popularity": 88.026,
                    "origin_country": [
                        "US"
                    ],
                    "vote_count": 3338,
                    "first_air_date": "2008-01-20",
                    "backdrop_path": "/eSzpy96DwBujGFj0xMbXBcGcfxX.jpg",
                    "original_language": "en",
                    "id": 1396,
                    "vote_average": 8.4,
                    "overview": "When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
                    "poster_path": "/1yeVJox3rjo2jBKrrihIMj7uoS9.jpg"
                }
            ]
        }, response.data)
    
    def test_get_title_400(self):
        """
        Ensure GET without query or titleName parameter evokes 400
        """
        urlEmptyParams = [
            "?query=",
            "?titleName=",
            "?query=&titleName=",
            "?titleName=&query=",
        ]
        for params in urlEmptyParams:
            response = self.client.get(self.api_title_url + params)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_method_title_405(self):
        """
        Ensure non-GET returns 405
        """
        methods = [
            (self.client.delete,'DELETE'),
            (self.client.post,'POST'),
            (self.client.put, 'PUT'),
        ]
        for method, methodStr in methods:
            response = method(self.api_title_url)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
            self.assertEqual(response.data, {'detail': ErrorDetail(string='Method \"' + methodStr + '\" not allowed.', code='method_not_allowed')})