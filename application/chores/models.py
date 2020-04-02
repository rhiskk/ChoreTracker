from application import db
from application.models import Base

from sqlalchemy.sql import text

class Chore(Base):
    name = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    instances = db.relationship("Instance", backref='chore', lazy=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)

    def __init__(self, name, points, groupId):
        self.name = name
        self.points = points
        self.group_id = groupId