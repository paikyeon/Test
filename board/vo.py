from member.vo import db

class Board(db.Model):
    num = db.Column(db.Integer, primary_key=True) #글번호. 자동생성
    #외래참조컬럼
    writer = db.Column(db.String(20), db.ForeignKey('member.id', ondelete='CASCADE'))

    #역참조. 작성자로 검색
    member = db.relationship('Member', backref=db.backref('board_set'))
    w_date = db.Column(db.DateTime(), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)