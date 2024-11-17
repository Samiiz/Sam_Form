from flask import render_template, request, redirect, Blueprint, session, url_for, jsonify
from views import users

routes = Blueprint('routes', __name__, template_folder='templates', url_prefix='/')


@routes.route('/')
def index():
    return render_template('index.hrml')

@routes.route('/signup', methods=['POST'])
def signup():
    user, reponse = users.create_user()
    return jsonify({"message": f"{user.name}님 회원가입을 축하합니다"}), 201
