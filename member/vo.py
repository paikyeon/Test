from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

#멤버(회원관리). vo, table
class Member(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pwd = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)