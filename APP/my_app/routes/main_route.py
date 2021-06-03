from flask import Blueprint, request, render_template
from my_app.models.user_model import get_users

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html'), 200

@bp.route('/user')
def user_index():
    return render_template('user.html'), 200

@bp.route('/del/user')
def deluser_index():
    return render_template('deluser.html'), 200

@bp.route('/res/user')
def result_index():
    return render_template('result.html'), 200