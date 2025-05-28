from app import create_app
from app.models import db, Employer, Employee
from faker import Faker
import random

app = create_app()
fake = Faker()

with app.app_context():
    print("Seeding database...")

    # Clear old data
    Employee.query.delete()
    Employer.query.delete()

    # Create 10 employers
    employers = []
    for _ in range(10):
        employer = Employer(name=fake.company(), industry=fake.job())
        employers.append(employer)
        db.session.add(employer)
    db.session.commit()

    # Create 50 employees assigned to random employers
    for _ in range(50):
        employee = Employee(
            name=fake.name(),
            position=fake.job(),
            employer_id=random.choice(employers).id
        )
        db.session.add(employee)
    db.session.commit()

    print("✅ Database seeded with 10 employers and 50 employees.")
