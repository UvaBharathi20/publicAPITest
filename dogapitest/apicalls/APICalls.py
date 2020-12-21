# import HandleRequestCalls
import random
import sys

from dogapitest.apicalls.HandleRequestCalls import *
from dogapitest.utils.URI_Constants import *
from dogapitest.utils.Constants import *


class DogAPIEndPoints(object):
    """

    """

    def get_response(self, end_point):
        """

        :param end_point:
        :return:
        """
        response = HandleRequests()
        return response.get_response_json(end_point)

    def get_list_of_all_breeds(self):
        """

        :return:
        """
        return self.get_response(LIST_ALL_BREEDS)

    def get_single_random_image_from_all(self):
        """

        :return:
        """
        return self.get_response(RANDOM_IMAGE_FROM_ALL_DOGS_COLLECTION)

    def get_multiple_random_image_from_all(self, is_rand=False, count_value=0):
        """

        :param count_value:
        :param rand:
        :return:
        """
        if is_rand:
            count = random.randint(MIN_VALUE_RANDOM_IMAGE_API, MAX_VALUE_RANDOM_IMAGE_API)
        else:
            count = count_value
        final_uri = RANDOM_IMAGES_FROM_ALL_DOGS_WITH_COUNT + str(count)
        dict = self.get_response(final_uri)
        dict['imagecount'] = count
        return dict

    def get_all_and_random_result_by_breed(self, is_all=True, is_random=False):
        breed = self.choose_random_breed()
        if is_all:
            final_uri = LIST_OF_ALL_IMAGES_BY_BREED + breed + IMAGES
        elif is_random:
            final_uri = LIST_OF_ALL_IMAGES_BY_BREED + breed + IMAGES_RANDOM

        dictt = self.get_response(final_uri)
        dictt['chosen_breed'] = breed
        return dictt

    def get_multiple_result_by_breed(self, breed, is_within_range=True,is_zero=False):
        res = self.get_response(LIST_OF_ALL_IMAGES_BY_BREED + breed + IMAGES)
        max = len(res['json']['message'])
        if is_within_range:
            count = random.randint(MIN_VALUE_RANDOM_IMAGE_API + 1, max)
        elif is_zero:
            count = 0
        else:
            count = random.randint(max + 1, sys.maxsize)
        final_uri = LIST_OF_ALL_IMAGES_BY_BREED + breed + IMAGES_RANDOM + "/" + str(count)
        dictt = self.get_response(final_uri)
        dictt['imagecount'] = count
        dictt['breed_length'] = max
        return dictt

    def choose_random_breed(self):
        response = self.get_list_of_all_breeds()
        breed = random.choice(list(response['json']['message']))
        return breed
