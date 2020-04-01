from application import db
from application.models import Base


##Association table
userGroup = db.Table('userGroup',
    db.Column('user_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
)

class Group(Base):

    __tablename__ = "group"

    name = db.Column(db.String(144), nullable=False)
    chores = db.relationship("Chore", backref='group', lazy=True)
    members = db.relationship('User', secondary=userGroup, backref=db.backref('groups', lazy=True))
    creator_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name