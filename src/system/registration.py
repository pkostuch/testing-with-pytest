import logging
from dataclasses import dataclass
from typing import Optional

import requests

logger = logging.getLogger('system')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


@dataclass
class User:
    uid: str
    name: str
    email: str


class NoConnectionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class MailService:

    def __init__(self, smtp_server: str):
        self.__smtp_server = smtp_server

    def send_greetings(self, email, name) -> None:
        logger.info(f'sending greeting email to {name} at {email}')


class Backend:
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port

    def __make_uri(self) -> str:
        return f'http://{self.__host}:{self.__port}'

    def find_user(self, name) -> Optional[User]:
        try:
            response = requests.get(f'{self.__make_uri()}/users/{name}')
            if response.status_code == 200:
                return User('abcd-0012', name, '')
            else:
                return None
        except requests.exceptions.ConnectionError as e:
            raise NoConnectionError(f'No connection to {self.__make_uri()}')

    def create_user(self, name, email) -> Optional[User]:
        try:
            response = requests.post(f'{self.__make_uri()}/users/{name}', data={'email': email})
            if response.status_code == 200:
                return User(response.headers.get('location', ''), name, email)
        except requests.exceptions.ConnectionError as e:
            raise NoConnectionError(f'No connection to {self.__make_uri()}')


class Registration:

    def __init__(self, backend, mail_service):
        self.__backend = backend
        self.__mail_service = mail_service

    # def __init__(self):
    #     self.__backend = Backend('localhost', 9999)
    #     pass

    def create_new_user(self, name: str, email: str):
        try:
            logger.info(f'checking if user {name} already exists')
            user = self.__backend.find_user(name)
            if user:
                logger.info(f'user {name} already registered')
                return False
            logger.info(f'creating user {name}, email {email}')
            self.__backend.create_user(name)
            logger.info(f'sending greetings to {name}')
            self.__mail_service.send_greetings(email, name)
            return True
        except NoConnectionError as e:
            raise e


if __name__ == '__main__':
    registration = Registration(Backend('localhost', 9999))
    registration.create_new_user('Bob', 'bob@gmail.com')
