# -*- coding:utf-8 -*-

from flask import render_template, redirect, url_for
from .forms import PostForm
from . import main
from ..models import Post
from .. import db


@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts)


@main.route('/edit', methods=['Get', 'Post'])
def edit_blog():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data)
        db.session.add(post)
        return redirect(url_for('.index'))
    return render_template('edit.html', form=form)


@main.route('/archive/<int:id>')
def get_article(id):
    article = Post.query.get_or_404(id)
    return render_template('post.html', article=article)
