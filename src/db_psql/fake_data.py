from faker import Faker
import random



def generate_data():
    fake = Faker()
    list_rows = []
    nb_row = random.randint(1000, 1200)
    for i in range(nb_row):
        list_rows.append(
            (i, fake.first_name(), fake.last_name(), fake.job(), fake.address(), fake.phone_number() )
        )
    return list_rows




    



