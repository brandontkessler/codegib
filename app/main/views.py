from flask import render_template, Blueprint
from flask_login import login_required
from app.decorators import check_confirmed

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route("/secret")
@login_required
@check_confirmed
def secret():
    return "SECRET PAGE"
