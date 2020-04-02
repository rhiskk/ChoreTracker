from application import db
from application.models import Base

from sqlalchemy.sql import text

##Association table
userGroup = db.Table('userGroup',
    db.Column('user_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
)

class Group(Base):

    name = db.Column(db.String(144), nullable=False)
    chores = db.relationship('Chore', backref='group', lazy=True)
    members = db.relationship('User', secondary=userGroup, backref=db.backref('groups', lazy=True))
    creator_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, creatorId):
        self.name = name
        self.creator_id = creatorId

    @staticmethod
    def find_creator_usernames():
        stmt = text('SELECT "Group".name, "Group".id, Account.username FROM Account, "Group"'
                    'WHERE "Group".creator_id = Account.id')
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0],"id":row[1], "creatorname":row[2]})
        
        return response