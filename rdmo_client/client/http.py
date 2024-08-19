import requests
from requests.exceptions import JSONDecodeError as RequestsJSONDecodeError
#from json import JSONDecodeError


class HTTPClient(object):

    def __init__(self, base_url, auth, headers):
        self.base_url, self.auth, self.headers = base_url, auth, headers

    def parse_response(self, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            try:
                print(response.json())
            except (RequestsJSONDecodeError):
                print(response.content)
            raise e
        try:
            response_return = response.json()
        except (RequestsJSONDecodeError):
            response_return = response.content
        return response_return

    def get(self, url, params={}):
        response = requests.get(self.base_url + url, params=params, auth=self.auth, headers=self.headers)
        return self.parse_response(response)

    def post(self, url, data):
        response = requests.post(self.base_url + url, data, auth=self.auth, headers=self.headers)
        return self.parse_response(response)

    def put(self, url, data):
        response = requests.put(self.base_url + url, data, auth=self.auth, headers=self.headers)
        return self.parse_response(response)

    def patch(self, url, data):
        response = requests.patch(self.base_url + url, json=data, auth=self.auth, headers=self.headers)
        return self.parse_response(response)

    def delete(self, url):
        response = requests.delete(self.base_url + url, auth=self.auth, headers=self.headers)
        return self.parse_response(response)
