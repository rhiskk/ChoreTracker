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

    def count_user_group_points(groupId):
        stmt = text('SELECT Account.username, COALESCE(SUM(Chore.points), 0)'
                    ' FROM (SELECT Account.username, Account.id  FROM Usergroup, Account, Gang'
                    ' WHERE Account.id = Usergroup.user_id AND Gang.id = Usergroup.group_id'
                    ' AND Gang.id = :groupId) Account'
                    ' LEFT JOIN Instance ON Account.id = Instance.account_id'
                    ' LEFT JOIN (SELECT id, points FROM Chore WHERE group_id = :groupId) Chore ON'
                    ' Instance.chore_id = Chore.id GROUP BY Account.username;'
                    ).params(groupId=groupId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"username":row[0], "points":row[1]})
        
        return response

    def count_user_total_points(userId):
        stmt = text('SELECT COALESCE(SUM(Chore.points), 0) FROM Account'
                    ' LEFT JOIN Instance ON Instance.account_id = Account.id'
                    ' LEFT JOIN Chore ON Instance.chore_id = Chore.id'
                    ' WHERE Account.id = :userId;'
                    ).params(userId=userId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"total":row[0]})
        
        return response

    def count_user_avg_points_per_group(userId):
        stmt = text('SELECT ROUND(AVG(Points.sum), 1) FROM'
                    ' (SELECT (COALESCE(SUM(Chore.points), 0)) sum, Chore.group_id FROM Account'
                    ' LEFT JOIN Instance ON Instance.account_id = Account.id'
                    ' LEFT JOIN Chore ON Instance.chore_id = Chore.id'
                    ' WHERE Account.id = :userId GROUP BY Chore.group_id) Points;'
                    ).params(userId=userId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"avg":row[0]})
        
        return response