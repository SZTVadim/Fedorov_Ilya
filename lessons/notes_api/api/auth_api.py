
from .base_api import BaseAPI


class AuthAPI(BaseAPI):

    def register(self, email, password, username):
        data = {
            "email": email,
            "password": password,
            "username": username
        }
        return self.post("/api/register", data=data)

    def login(self, email, password):
        data = {
            "email": email,
            "password": password
        }
        return self.post("/api/login", data=data)
