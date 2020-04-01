from application import db
from application.models import Base

class Chore(Base):
    
    name = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    instances = db.relationship("Instance", backref='chore', lazy=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)

    def __init__(self, name, points):
        self.name = name
        self.points = points