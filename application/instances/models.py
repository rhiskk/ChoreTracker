from application import db

class Instance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    chore_id = db.Column(db.Integer, db.ForeignKey('chore.id'), nullable=False)

    def __init__(self, accountId, choreId):
        self.account_id = accountId
        self.chore_id = choreId