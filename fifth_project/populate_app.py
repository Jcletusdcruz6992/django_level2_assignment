import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fifth_project.settings')

import django
django.setup()

import random
from james_app.models import User
from faker import Faker
fakegen=Faker()

def populate(N=5):
    fake_name=fakegen.name().split()
    fake_firstname=fake_name[0]
    fake_lastname=fake_name[1]
    fake_email=fakegen.email()
    for x in range(N):
        User.objects.get_or_create(First_name=fake_firstname,Last_name=fake_lastname,email=fake_email)[0]

if __name__ == '__main__':
    print('Populating script')
    populate(10)
    print('Populating  completed !')
