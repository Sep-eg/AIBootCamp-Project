from flask import Blueprint, request, redirect, url_for, render_template
from my_app.models import user_model
from my_app.utils import main_funcs

bp = Blueprint('user', __name__)

@bp.route('/user', methods=['POST'])
def add_user():

    raw_user = request.form

    result = user_model.add_user(raw_user)
    return redirect(url_for('main.user_index',msg=result), code=200)

@bp.route('/del/user', methods=['POST'])
def delete_user():

    raw_user = request.form

    result = user_model.delete_user(raw_user)

    if result == 1:
        return redirect(url_for('main.deluser_index'), code=200)
    elif result == 2:
        return "일치하는 ID가 없습니다.", 400
    else:
        return "일치하는 ID 혹은 별명이 없습니다.", 400

@bp.route('/res/user', methods=['POST'])
def result():

    raw_user = request.form

    # raw_user = {
    #             'id' : request.form.get('id'),
    #             'nickname' : request.form.get('nickname')
    # }

    age, user = user_model.get_users(raw_user)

    if user == 0:
        return age, 400
    if age == 0:
        return user, 400
        

    result = main_funcs.predict_life(age, user)

    return render_template('respage.html', result = result), 200
