# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    #tags = StringField(validators=[InputRequired()])
    category = StringField(validators=[InputRequired()])
    body = TextAreaField(validators=[InputRequired()])
    summary = TextAreaField(validators=[InputRequired()])
    submit = SubmitField("Submit")
