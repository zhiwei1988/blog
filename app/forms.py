# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    body = TextAreaField("new blog")
    # body = TextAreaField("new blog", validators=[DataRequired])
    submit = SubmitField("Submit")