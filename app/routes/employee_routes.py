from flask import request
from flask_restful import Resource
from ..models.employee import Employee
from ..models.employer import Employer
from ..models import db

class EmployeeListResource(Resource):
    def get(self):
        employees = Employee.query.all()
        return [{'id': e.id, 'name': e.name, 'position': e.position, 'employer_id': e.employer_id} for e in employees]

    def post(self):
        data = request.get_json()
        default_employer = Employer.query.first()
        if not default_employer:
            return {'message': 'No employer found. Seed the database first.'}, 400

        new_employee = Employee(
            name=data['name'],
            position=data['position'],
            employer_id=default_employer.id
        )
        db.session.add(new_employee)
        db.session.commit()
        return {'message': 'Employee created', 'id': new_employee.id}, 201

class EmployeeResource(Resource):
    def get(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        return {'id': employee.id, 'name': employee.name, 'position': employee.position, 'employer_id': employee.employer_id}

    def put(self, employee_id):
        data = request.get_json()
        employee = Employee.query.get_or_404(employee_id)
        employee.name = data.get('name', employee.name)
        employee.position = data.get('position', employee.position)
        db.session.commit()
        return {'message': 'Employee updated'}

    def delete(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return {'message': 'Employee deleted'}
