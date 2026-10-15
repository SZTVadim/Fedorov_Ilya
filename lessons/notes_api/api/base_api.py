
import requests


class BaseAPI:
    def __init__(self):
        self.base_url = "http://185.240.103.201:8000"

    def get(self, endpoint, headers=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=headers
        )

    def post(self, endpoint, data=None, headers=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def delete(self, endpoint, headers=None):
        return requests.delete(
            f"{self.base_url}{endpoint}",
            headers=headers
        )
