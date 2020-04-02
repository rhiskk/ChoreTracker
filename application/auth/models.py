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

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def count_user_total_points(groupId):
        stmt = text('SELECT DISTINCT ON(Chore.group_id) Account.username, SUM(Chore.points) FROM Account'
                    ' LEFT JOIN Instance ON Instance.account_id = Account.id'
                    ' LEFT JOIN Chore ON Chore.id = Instance.chore_id'
                    ' GROUP BY Account.id HAVING Chore.group_id = :groupId'
                    ).params(groupId=groupId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"username":row[0], "points":row[1]})
        
        return response