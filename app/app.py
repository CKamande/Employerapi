from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .models import db
from .routes.employee_routes import EmployeeResource, EmployeeListResource

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    # Register API endpoints
    api.add_resource(EmployeeListResource, '/employees')
    api.add_resource(EmployeeResource, '/employees/<int:employee_id>')

    # Root route
    @app.route('/')
    def index():
        return {"message": "Welcome to the Employer-Employee API"}, 200

    return app
