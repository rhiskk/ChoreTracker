from application import db
from application.models import Base

from sqlalchemy.sql import text

##Association table
userGroup = db.Table('usergroup',
    db.Column('user_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('gang.id'))
)

class Group(Base):

    __tablename__ = 'gang'

    name = db.Column(db.String(144), nullable=False)
    chores = db.relationship('Chore', backref='gang', lazy=True)
    members = db.relationship('User', secondary=userGroup, backref=db.backref('groups', lazy=True))
    creator_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, creatorId):
        self.name = name
        self.creator_id = creatorId

    @staticmethod
    def find_users_groups(userId):
        stmt = text('SELECT Gang.name, Gang.id, a.username FROM Gang'
                    ' LEFT JOIN userGroup ug ON Gang.id = ug.group_id'
                    ' LEFT JOIN Account a ON Gang.creator_id = a.id'
                    ' WHERE ug.user_id = :userId').params(userId=userId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0],"id":row[1], "creatorname":row[2]})
        
        return response

    def find_non_users_groups(userId):
        stmt = text('SELECT Gang.name, Gang.id, a.username FROM Gang'
                    ' LEFT JOIN userGroup ug ON Gang.id = ug.group_id'
                    ' LEFT JOIN Account a ON Gang.creator_id = a.id'
                    ' GROUP BY Gang.id, Gang.name, a.username'
                    ' HAVING Gang.id NOT IN (SELECT Gang.id FROM Gang' 
                    ' LEFT JOIN userGroup ug ON Gang.id = ug.group_id'
                    ' WHERE ug.user_id = :userId)').params(userId=userId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0],"id":row[1], "creatorname":row[2]})
        
        return response

    @staticmethod
    def find_creator_usernames():
        stmt = text('SELECT Gang.name, Gang.id, Account.username FROM Account, Gang'
                    ' WHERE Gang.creator_id = Account.id')
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0],"id":row[1], "creatorname":row[2]})
        
        return response