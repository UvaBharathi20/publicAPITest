import requests


class HandleRequests:
    def get_response_for_endpoint(self,end_point):
        # api-endpoint
        URL = end_point

        # sending get request and saving the response as response object
        response = requests.get(url=URL)
        return response

    def get_response_json(self, end_point):
        """
        :param end_point: URL to hit
        :return: the json response of endpoint.
        """
        # api-endpoint
        data = self.get_response_for_endpoint(end_point)
        response_dict = {}
        response_dict['response'] = data
        response_dict['json'] = data.json()
        return response_dict
