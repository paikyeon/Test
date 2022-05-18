from flask import request, render_template, redirect, Blueprint, session

bp = Blueprint('upload', __name__, url_prefix='/upload')

@bp.route('/form')
def upload_form():
    return render_template('upload/form.html')

@bp.route('/upload', methods=['POST'])
def upload():
    upload_path = 'static/img/'
    f = request.files['file']
    fname = upload_path+f.filename #f.filename:업로드된 파일명
    f.save(fname)
    fname = '/' + fname
    return render_template('upload/img_list.html', img_path=fname)