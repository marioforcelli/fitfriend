import pytest
from unittest.mock import MagicMock
from datetime import datetime

from src.domain.entities.user import User
from src.application.use_cases  import UserUseCases

def test_user_use_case_create():
    user_mock = {
        "email": "fulano@ciclano.com",
        "full_name": "Fulano de Tal",
        "weight": 70.5,
        "height": 1.75,
        "phone": "11123456789",
        "birth_date": "1990-01-01",
        "created_at": "2023-10-01T12:00:00",
        "updated_at": "2023-10-01T12:00:00"
    }

    user_mock = User(**user_mock)

    user_repository_mock = MagicMock()
    user_repository_mock.save.return_value = user_mock

    use_case = UserUseCases(user_repository_mock)

    result = use_case.create_user(user_mock)

    user_repository_mock.save.assert_called_once_with(user_mock)

    assert result.email == "fulano@ciclano.com"
    assert result.full_name == "Fulano de Tal"
    assert isinstance(result, User)

def test_user_use_case_get_by_email():

    user_mock = {
        "email": "fulano@ciclano.com",
        "full_name": "Fulano de Tal",
        "weight": 70.5,
        "height": 1.75,
        "phone": "11123456789",
        "birth_date": "1990-01-01",
        "created_at": "2023-10-01T12:00:00",
        "updated_at": "2023-10-01T12:00:00"
    }
    
    email = "fulano@ciclano.com"

    user_repo_mock = MagicMock()
    user_repo_mock.find_by_email.return_value = User(**user_mock)

    use_case = UserUseCases(user_repo_mock)

    result = use_case.get_user_by_email(email)

    user_repo_mock.find_by_email.assert_called_once_with(email)

    assert result.email == "fulano@ciclano.com"
    assert result.full_name == "Fulano de Tal"
    assert isinstance(result, User)

