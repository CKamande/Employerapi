import random
from faker import Faker
from .models import db
from .models.employer import Employer
from .models.employee import Employee

fake = Faker()

def seed_data(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        employers = [Employer(name=fake.company()) for _ in range(10)]
        db.session.add_all(employers)
        db.session.commit()

        for _ in range(50):
            employee = Employee(
                name=fake.name(),
                position=fake.job(),
                employer_id=random.choice(employers).id
            )
            db.session.add(employee)

        db.session.commit()
        print("Seeded 10 employers and 50 employees.")
