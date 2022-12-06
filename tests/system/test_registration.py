import pytest
from unittest.mock import Mock, MagicMock

from system.registration import Registration, Backend, User, MailService


@pytest.fixture()
def setup():
    backend = Mock(spec=Backend)
    backend.find_user.return_value = None
    backend.create_user.return_value = User('0001-0ab1', 'Bob', 'bob@gmail.com')
    mail_service = Mock(spec=MailService)
    return Registration(backend, mail_service), backend, mail_service


def test_registration():
    backend = Mock()
    backend.find_user.return_value = User('001', 'Bob', 'bob@yahoo.com')
    backend.create_user.return_value = None
    registration = Registration(backend)
    backend.find_user.assert_called()
    backend.find_user.assert_called_with('Bob')


def test_registration_with_fixture(setup):
    registration, backend, mail_service = setup
    assert registration.create_new_user('Bob', 'bob@gmail.com')
    backend.find_user.assert_called_with('Bob')
    backend.create_user.assert_called
    mail_service.send_greetings.assert_called_with('bob@gmail.com', 'Bob')



class Operator:

    def create(self):
        pass

    def delete(self):
        pass


def test_mock():
    crud_mock = Mock()
    crud_mock.create()
    crud_mock.delete()


def test_mock_():
    crud_mock = Mock(spec=['create', 'delete'])
    crud_mock.get()
