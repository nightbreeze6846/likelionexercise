# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    SelectField
)
from wtforms import validators
from wtforms.fields.html5 import (
    EmailField,
    DateField
)
class HistoryAddForm(Form):
    title = StringField(
        u'경력',
        [validators.data_required(u'경력을 입력하시기 바랍니다.')],
        description={'placeholder': u'무슨 일을 하셨나요?'}
    )
    tag = SelectField(u'종류', choices=[('award', u'수상'), ('event', u'공연'), ('misc', u'기타')])

    starttime = DateField(
        u'언제부터',
        [validators.data_required(u'기간을 선택하시기 바랍니다.')]
    )
    endtime = DateField(
        u'',
        [validators.data_required(u'기간을 선택하시기 바랍니다.')]
    )
    content = TextAreaField(
        u'언제까지',
        [validators.data_required(u'설명을 입력하시기 바랍니다.')],
        description={'placeholder': u'어떤 일을 하셨는지 자세히 설명해주세요.'}
    )

class JoinForm(Form):
    email = EmailField(
        u'이메일',
        [validators.data_required(u'이메일을 입력하시기 바랍니다.')],
        description={'placeholder': u'이메일을 입력하세요.'}
    )
    password = PasswordField(
        u'패스워드',
        [validators.data_required(u'패스워드를 입력하시기 바랍니다.'),
        validators.EqualTo('confirm_password', message=u'패스워드가 일치하지않습니다.')],
        description={'placeholder': u'패스워드를 입력하세요.'}
    )
    confirm_password = PasswordField(
        u'패스워드 확인',
        [validators.data_required(u'패스워드를 한번 더 입력하세요.')],
        description={'placeholder': u'패스워드를 한번 더 입력하세요.'}
    )
    name = StringField(
        u'이름',
        [validators.data_required(u'이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'뮤지션(혹은 그룹) 이름을 입력해주세요.'}
    )
    birthday = DateField(
        u'생일',
        [validators.data_required(u'생일을 입력하시기 바랍니다.')]
    )
    

class LoginForm(Form):
    email = EmailField(
        u'이메일',
        [validators.data_required(u'이메일을 입력해주세요.')],
        description={'placeholder': u'이메일을 입력하세요.'}
    )
    password = PasswordField(
        u'패스워드',
        [validators.data_required(u'패스워드를 입력해주세요.')],
        description={'placeholder': u'패스워드를 입력하세요.'}
    )