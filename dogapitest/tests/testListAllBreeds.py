import unittest
from dogapitest.apicalls.APICalls import DogAPIEndPoints

class TestListAllBreeds(unittest.TestCase):
    """
    https://dog.ceo/dog-api/documentation/
    Validate the list of dog breeds api.
    """
    def setUp(self):
        self.dog_api_endpoint = DogAPIEndPoints()

    def test_list_all_breeds(self):
        """
        Test case : List all breeds
        check response status, response code and length value of list of dags should not be zero.
        """
        response = self.dog_api_endpoint.get_list_of_all_breeds()
        # validate response code
        self.assertEqual(str(response['response'].status_code), '200', 'Validate  HTTP 200 OK success status response')

        # validate the json message
        self.assertEqual(response['json']['status'], 'success', "Validation for message status")

        # validate dog list size greater than zero
        self.assertTrue(len(response['json']['message']) > 0, "The dogs breed list size validation")
