import sys
import unittest
from random import randint

from dogapitest.apicalls.APICalls import DogAPIEndPoints
from dogapitest.utils.Constants import *


class TestRandomImageFromAll(unittest.TestCase):
    def setUp(self):
        self.dog_api_endpoint = DogAPIEndPoints()

    def test_multiple_random_image_from_all(self):
        """
        https://dog.ceo/dog-api/documentation/random
        Validate the random image display from all dog list
        """
        response = self.dog_api_endpoint.get_multiple_random_image_from_all(True)
        # Validate HTTP response code
        self.assertEqual(str(response['response'].status_code), '200', 'Validate  HTTP 200 OK success status response')

        # validate the json message
        self.assertEqual(response['json']['status'], 'success', "Validation for message status")

        # Validate input count result
        count = response['imagecount']
        self.assertEqual(count, len(response['json']['message']), "Total images returned should be equal to count")


    def test_multiple_random_image_from_all_for_zero_count(self):
        """
        Test case : List multiple image based on count provided. Pass count =0.
        check response status, response code and always 1 random image should be returned..
        """
        response = self.dog_api_endpoint.get_multiple_random_image_from_all(False)
        # Validate HTTP response code
        self.assertEqual(str(response['response'].status_code), '200', 'Validate  HTTP 200 OK success status response')

        # validate the json message
        self.assertEqual(response['json']['status'], 'success', "Validation for message status")
        # Validate output image list size for 0 input
        self.assertEqual(1, len(response['json']['message']), "Total images returned should be 1 for zero count")

    def test_multiple_random_image_from_all_for_zero_count(self):
        """
        Test case : List multiple image based on count provided. Pass count > max.
        check response status, response code and always the max size should be displayed if count > max.
        """
        response = self.dog_api_endpoint.get_multiple_random_image_from_all(False,
                                                                            randint(MAX_VALUE_RANDOM_IMAGE_API,
                                                                                    sys.maxsize))
        # Validate HTTP response code
        self.assertEqual(str(response['response'].status_code), '200', 'Validate  HTTP 200 OK success status response')

        # validate the json message
        self.assertEqual(response['json']['status'], 'success', "Validation for message status")

        # Validate output image list size for input size > max allowed size
        self.assertEqual(MAX_VALUE_RANDOM_IMAGE_API, len(response['json']['message']), "Total images returned should "
                                                                                       "be max size for values > max "
                                                                                       "size")

    def test_single_random_image_from_all(self):
        """
        Test case : List single image from all the dogs collection.
        check response status, response code and length value of output is always 1 so string.
        """
        response = self.dog_api_endpoint.get_single_random_image_from_all()
        # Validate HTTP response code
        self.assertEqual(str(response['response'].status_code), '200', 'Validate  HTTP 200 OK success status response')

        # validate the json message
        self.assertEqual(response['json']['status'], 'success', "Validation for message status")

        # Validate input count result
        self.assertTrue(type(response['json']['message']) == str,
                        "Total images returned should always be 1 so the value will be string")
