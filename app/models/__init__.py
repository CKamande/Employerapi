from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .employer import Employer
from .employee import Employee

__all__ = ["db", "Employer", "Employee"]
