from flask import Flask, render_template, request, redirect, session
import matplotlib.pyplot as plt
from member.vo import db, migrate
import routes.mem_route as mr
import routes.board_route as br
import pandas as pd






from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/HMFMPYUN.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

app = Flask(__name__)  #웹 어플리케이션





import config   #컨피그 파일(config.py) import

#플라스크 객체 생성
app = Flask(__name__)

#시크릿 키 생성
app.secret_key = 'tyiyuuo'

#플라스크 컨피그에 사용자정의 컨피그 추가
app.config.from_object(config)

#블루 프린트 등록
app.register_blueprint(mr.bp)
app.register_blueprint(br.bp)


# ORM 연동
db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def root():
    if 'flag' not in session.keys():
        session['flag']=False
    return render_template('index.html')

@app.route('/graph')
def graph():
    df = pd.read_csv('관중통계(전체현황) - 관중통계(전체현황).csv', encoding='cp949')
    df= df.sort_values(by='월')
    df = df[['월', '관중수']]

    # plot
    plt.figure(figsize=(9, 7))
    plt.rcParams.update({'font.size': 22})
    ax = df.set_index('월')['관중수'].plot(kind='line', marker='d')
    ax.set_ylabel("관중수")
    ax.set_xlabel("월")
    plt.show()

if __name__ == '__main__':
    app.run()