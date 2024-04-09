import os
import dataclasses
from dotenv import load_dotenv


def load_env():
    load_dotenv()


load_env()


@dataclasses.dataclass
class User:
    email: str
    password: str
    budget_from_filter: int


test_user = User(
        email=os.getenv('LOGIN_USER'),
        password=os.getenv('PASSWORD_USER'),
        budget_from_filter=100000
        )

# class TestData():
#
#     target_value_price_filter = 100000