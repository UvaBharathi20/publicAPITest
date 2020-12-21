from dogapitest.apicalls.HandleRequestCalls import HandleRequests


class CheckResponseOFImage(object):
    """

    """

    def get_response(self, end_point):
        response = HandleRequests()
        return response.get_response_json(end_point)

    def check_response_of_images(self, message):
        if type(message) == list:
            for i in message:
                print(self.get_response(i))
