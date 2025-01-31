import requests

from faker import Faker
from urls import *


def new_user_body():
    fake = Faker()
    return {"email": fake.email(), "password": fake.password(), "name": fake.name()}


def create_new_user():
    new_user = new_user_body()
    response = requests.post(f'{BASE_URL}/{API_REGISTER}', data=new_user)
    return new_user, response


def delete_user(token):
    response = requests.delete(f'{BASE_URL}/{API_USER}', headers=token)
    return response
