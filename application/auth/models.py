from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = 'account'

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    instances = db.relationship('Instance', backref='account', lazy=True)
    created_groups = db.relationship('Group', backref='account', lazy=True)
    role = db.Column(db.String(144), nullable=False)

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.role

    def count_user_total_points(groupId):
        stmt = text('SELECT Account.username, COALESCE(SUM(Chore.points), 0) FROM Account'
                    ' LEFT JOIN Usergroup ug ON ug.user_id = account.id'
                    ' LEFT JOIN Gang ON ug.group_id = Gang.id'
                    ' LEFT JOIN Instance ON Account.id = Instance.account_id'
                    ' LEFT JOIN Chore ON Instance.chore_id = Chore.id'
                    ' WHERE Gang.id = :groupId GROUP BY Account.id;'
                    ).params(groupId=groupId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"username":row[0], "points":row[1]})
        
        return response