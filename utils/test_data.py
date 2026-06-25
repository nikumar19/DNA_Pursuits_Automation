from faker import Faker

fake = Faker()
client_name = fake.company()
pursuit_name = fake.catch_phrase()
jupiter_id = fake.random_int(min=100000, max=999999)
