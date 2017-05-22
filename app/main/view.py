# -*- coding:utf-8 -*-

from flask import render_template, redirect, url_for
from .forms import PostForm
from . import main
from ..models import Post
from .. import db


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/edit', methods=['Get', 'Post'])
def edit_blog():
    form = PostForm()
    if form.is_submitted():
        post = Post(body=form.body.data)
        db.session.add(post)
        return redirect(url_for('.index'))
    return render_template('edit.html', form=form)