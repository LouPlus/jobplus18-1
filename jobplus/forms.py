from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, DataRequired
from .models import db, User

class UserRegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3,24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.usernmae = self.username.data
        user.email = self.email.data
        user.password = slef.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

class CompanyRegisterForm(FlaskForm):
    username = StringField('企业名称', validators=[DataRequired(), Length(3,24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.usernmae = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        user.role = user.ROLE_COMPANY
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

class LoginForm(FlaskForm):
	email = StringField('邮箱', validators=[DataRequired(), Email()])
	password = PasswordField('密码', validators=[DataRequired(), Length(6,24)])
	remember_me = BooleanField('记住我')
	submit = SubmitField('提交')


