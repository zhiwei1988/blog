# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    body = TextAreaField(validators=[InputRequired()])
    submit = SubmitField("Submit")
