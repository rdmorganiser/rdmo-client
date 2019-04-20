import requests


class HTTPClient(object):

    def __init__(self, base_url, auth, headers):
        self.base_url, self.auth, self.headers = base_url, auth, headers

    def parse_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(response.json())
            raise e

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
