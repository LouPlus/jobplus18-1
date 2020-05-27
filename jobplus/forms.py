from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, TextAreaField
from wtforms.validators import Length, Email, EqualTo, DataRequired
from .models import db, User, CompanyDetail

class UserRegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3,24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6,24, message='密码长度要在6-24个字符之间')])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        self.populate_obj(user)
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
    password = PasswordField('密码', validators=[DataRequired(), Length(6,24, message='密码长度要在6-24个字符之间')])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        self.populate_obj(user)
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

class UserEditForm(FlaskForm):
    real_name = StringField('姓名')
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码(不填写保持不变)')
    phone = StringField('手机号', validators=[Regexp(r'1[34579]\d{9}', message='手机号格式错误')])
    work_years = IntegerField('工作年限')
    resume_url = StringField('简历地址')
    submit = SubmitField('提交')

    def update_user(self, user):
        user = User()
        user.real_name = self.real_name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        user.phone = self.phone.data
        user.work_years = self.work_years.data
        user.resume_url = self.resume_url.data
        db.session.add(user)
        db.session.commit()

class CompanyEditForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码(不填写保持不变)')
    phone = StringField('手机号', validators=[Regexp(r'1[34579]\d{9}', message='手机号格式错误')])
    slug = StringField('Slug', validators=[Length(3,24)])
    location = StringField('地址', validators=[Length(0,64)])
    site = StringField('公司网站', validators=[URL(message='网站格式错误')])
    logo = StringField('Logo')
    description = StringField('一句话描述', validators=[DataRequired(), Length(0,100)])
    about = TextAreaField('公司详情', validators=[Length(0,100)])
    submit = SubmitField('提交')

    def update_company(self,user):
        user = User()
        user.name = self.name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        if user.company_detail:
            company_detail = user.company_detail
        else:
            company_detail = CompanyDetail()
            company_detail.user_id = user.id
        self.populate_obj(company_detail)
        db.session.add(user)
        db.session.add(company_detail)
        db.session.commit()



