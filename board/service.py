from board.vo import Board
from datetime import datetime
from member.vo import db, Member

class BoardService:
    #글작성
    def addBoard(self, b:Board):#작성자id, title, content
        b.w_date = datetime.now()
        db.session.add(b)
        db.session.commit()

    def getBoard(self, num):
        return Board.query.get(num)#primary key로 검색

    def getAll(self):
        return Board.query.order_by(Board.num.desc())

    def getByTitle(self, tit):
        return Board.query.filter(Board.title.like('%'+tit+'%')).all()

    def getByWriter(self, writer):
        mem = Member.query.get(writer) #작성자 값으로 member 테이블에서 사람하나 검색
        if mem is not None:
            return mem.board_set #작성자가 쓴 모든 글 검색해서 반환

    def editBoard(self, b:Board):
        b2 = self.getBoard(b.num) #수정할 객체를 검색
        # 검색한 객체를 바로 수정 => db에서도 수정됨
        b2.title = b.title
        b2.content = b.content
        #b2.w_date = datetime.now()
        db.session.commit()

    def delBoard(self, num):#삭제할 객체를 검색
        b = self.getBoard(num)
        db.session.delete(b)#검색한 객체 삭제
        db.session.commit()