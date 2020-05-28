# _*_ coding : UTF-8 _*_
#开发人员 ： 纠结中的忐忑
#开发时间 ： 2020/5/26  19:33
#文件名称 ： admin.py.PY
#开发工具 ： PyCharm

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from jobplus.models import User


admin = Blueprint('admin', __name__, url_prefix='/admin')