import unittest
import random

from dogapitest.apicalls.APICalls import DogAPIEndPoints


class TestByBreedAPI(unittest.TestCase):
    """
    Class to run the test cases for by breed API
    https://dog.ceo/dog-api/documentation/breed
    """
    def setUp(self):
        self.dog_api_endpoint = DogAPIEndPoints()

    def test_retrun_all_images_for_breed(self):
        """
        Test case: Returns an array of all the images from a breed
        choose a random breed and pass to the api.
        check response status, resposne code and length value of list of images.
        """
        response = self.dog_api_endpoint.get_all_and_random_result_by_breed()
        # validate response code
        self.assertEqual(str(response['response'].status_code), '200', 'Validate  HTTP 200 OK success status response')

        # validate the json message
        self.assertEqual(response['json']['status'], 'success', "Validation for message status")

        # validate all images of breed list size greater than zero
        self.assertTrue(len(response['json']['message']) > 0, "The dogs breed list size validation")

    def test_return_random_single_image_for_breed(self):
        """
        Test case: check Returns a random dog image from a breed.
        choose a random breed and pass to the api.
        check response status, response code and length value of list of image is 1.
        """
        response = self.dog_api_endpoint.get_all_and_random_result_by_breed(False, True)
        # Validate HTTP response code
        self.assertEqual(str(response['response'].status_code), '200', 'Validate  HTTP 200 OK success status response')

        # validate the json message
        self.assertEqual(response['json']['status'], 'success', "Validation for message status")

        # Validate count result
        self.assertTrue(type(response['json']['message']) == str,
                        "Total images returned should always be 1 so the value will be string")

    def test_return_random_multiple_image_for_breed_input_greater_than_max(self):
        """
        Test case: check Return multiple random dog image from a breed for the input value passed.
        choose a random breed and pass to the api.
        pass value greater than the total image of the list.
        then all the images of the list should be given in output.
        check response status, response code and length value of list of image is 1.
        """
        choose_breed = self.dog_api_endpoint.choose_random_breed()
        response = self.dog_api_endpoint.get_multiple_result_by_breed(choose_breed, False)

        # Validate HTTP response code
        self.assertEqual(str(response['response'].status_code), '200', 'Validate  HTTP 200 OK success status response')

        # validate the json message
        self.assertEqual(response['json']['status'], 'success', "Validation for message status")
        count_of_images_in_breed = response['breed_length']
        input_count_provided = response['imagecount']
        #validate the length of images list
        if input_count_provided > count_of_images_in_breed:
            self.assertTrue(len(response['json']['message']) == count_of_images_in_breed,
                            "if the input value is greater than max length then return all images")
